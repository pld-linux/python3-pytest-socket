#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Pytest Plugin to disable socket calls during tests
Summary(pl.UTF-8):	Wtyczka pytesta blokująca odwołania do gniazd w trakcie testów
Name:		python3-pytest-socket
Version:	0.8.1
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-socket/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-socket/pytest_socket-%{version}.tar.gz
# Source0-md5:	eebfbef33da08f54c8665c9af98f8dff
URL:		https://pypi.org/project/pytest-socket/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.10
BuildRequires:	python3-uv-build >= 0.7.20
BuildRequires:	python3-uv-build < 0.13
%if %{with tests}
BuildRequires:	python3-anyio
BuildRequires:	python3-httpx >= 0.28.1
BuildRequires:	python3-pytest >= 7.0.0
# upstream uses pytest-codspeed; pytest-benchmark provides the same benchmark fixture
BuildRequires:	python3-pytest-benchmark
BuildRequires:	python3-starlette >= 0.47.1
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A plugin to use with Pytest to disable or restrict socket calls during
tests to ensure network calls are prevented.

%description -l pl.UTF-8
Wtyczka dla pytesta blokująca lub ograniczająca odwołania do gniazd
podczas testów, aby zapobiec odwołaniom do sieci.

%prep
%setup -q -n pytest_socket-%{version}

%build
%py3_build_pyproject

%if %{with tests}
# expects localhost to resolve to both 127.0.0.1 and ::1, depends on /etc/hosts
# the others connect to public hosts (google.com, http.codes), no network on builders
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=anyio.pytest_plugin,pytest_benchmark.plugin,pytest_socket \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest tests -k 'not (test_single_cli_arg_connect_disabled_hostname_resolved or test_parametrize_with_socket_enabled_and_allow_hosts or test_global_disable_and_allow_host or test_urllib_succeeds_by_default or test_enabled_urllib_succeeds)'
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/pytest_socket
%{py3_sitescriptdir}/pytest_socket-%{version}.dist-info
