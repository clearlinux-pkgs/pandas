#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v27
# autospec commit: 65cf152
#
Name     : pandas
Version  : 2.3.1
Release  : 143
URL      : https://github.com/pandas-dev/pandas/releases/download/v2.3.1/pandas-2.3.1.tar.gz
Source0  : https://github.com/pandas-dev/pandas/releases/download/v2.3.1/pandas-2.3.1.tar.gz
Summary  : Powerful data structures for data analysis, time series, and statistics
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT Python-2.0
Requires: pandas-license = %{version}-%{release}
Requires: pandas-python = %{version}-%{release}
Requires: pandas-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : meson
BuildRequires : pypi(cython)
BuildRequires : pypi(meson)
BuildRequires : pypi(meson_python)
BuildRequires : pypi(numpy)
BuildRequires : pypi(python_dateutil)
BuildRequires : pypi(pytz)
BuildRequires : pypi(versioneer)
BuildRequires : pypi(wheel)
BuildRequires : pypi-cython
BuildRequires : python3-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The Docker image here helps to set up an isolated environment containing a debug version of Python and a gdb installation which the Cython debugger can work with.

%package license
Summary: license components for the pandas package.
Group: Default

%description license
license components for the pandas package.


%package python
Summary: python components for the pandas package.
Group: Default
Requires: pandas-python3 = %{version}-%{release}

%description python
python components for the pandas package.


%package python3
Summary: python3 components for the pandas package.
Group: Default
Requires: python3-core
Provides: pypi(pandas)
Requires: pypi(numpy)
Requires: pypi(python_dateutil)
Requires: pypi(pytz)
Requires: pypi(tzdata)

%description python3
python3 components for the pandas package.


%prep
%setup -q -n pandas-2.3.1
cd %{_builddir}/pandas-2.3.1
pushd ..
cp -a pandas-2.3.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1752003943
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pandas
cp %{_builddir}/pandas-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pandas/292fa4730b512dc7a5a1cc97a83fe88d536ed1f8 || :
cp %{_builddir}/pandas-%{version}/LICENSES/DATEUTIL_LICENSE %{buildroot}/usr/share/package-licenses/pandas/f3b34c666d9f93071f6dbeeea6f8daefc2258e90 || :
cp %{_builddir}/pandas-%{version}/LICENSES/HAVEN_LICENSE %{buildroot}/usr/share/package-licenses/pandas/9d84be01def522d7ac0016e7ccf20bf0f56c74c4 || :
cp %{_builddir}/pandas-%{version}/LICENSES/KLIB_LICENSE %{buildroot}/usr/share/package-licenses/pandas/06b00648cfa95f2da750be33f7ea5d2fb070dece || :
cp %{_builddir}/pandas-%{version}/LICENSES/MUSL_LICENSE %{buildroot}/usr/share/package-licenses/pandas/a0386bf16298550823fe867827ba493445658bcc || :
cp %{_builddir}/pandas-%{version}/LICENSES/PSF_LICENSE %{buildroot}/usr/share/package-licenses/pandas/c6e195f9aa30cc9b675d1612ca4fb7f74111bd35 || :
cp %{_builddir}/pandas-%{version}/LICENSES/PYPERCLIP_LICENSE %{buildroot}/usr/share/package-licenses/pandas/9bc59dfb5518a0bf9fdac69028fb3c85b869a9e1 || :
cp %{_builddir}/pandas-%{version}/LICENSES/PYUPGRADE_LICENSE %{buildroot}/usr/share/package-licenses/pandas/38fde5cae5354d13aa716f58df8872cca48cb307 || :
cp %{_builddir}/pandas-%{version}/LICENSES/SAS7BDAT_LICENSE %{buildroot}/usr/share/package-licenses/pandas/2b4d2bae5f98f9cad6a84254dbd5faca415a9eb9 || :
cp %{_builddir}/pandas-%{version}/LICENSES/ULTRAJSON_LICENSE %{buildroot}/usr/share/package-licenses/pandas/6e23754cdd7f452bd9aa9c8b46a4796e5e2556c9 || :
cp %{_builddir}/pandas-%{version}/LICENSES/XARRAY_LICENSE %{buildroot}/usr/share/package-licenses/pandas/34774a54e4b286739f317922b31ba5eb3ec9195e || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pandas/06b00648cfa95f2da750be33f7ea5d2fb070dece
/usr/share/package-licenses/pandas/292fa4730b512dc7a5a1cc97a83fe88d536ed1f8
/usr/share/package-licenses/pandas/2b4d2bae5f98f9cad6a84254dbd5faca415a9eb9
/usr/share/package-licenses/pandas/34774a54e4b286739f317922b31ba5eb3ec9195e
/usr/share/package-licenses/pandas/38fde5cae5354d13aa716f58df8872cca48cb307
/usr/share/package-licenses/pandas/6e23754cdd7f452bd9aa9c8b46a4796e5e2556c9
/usr/share/package-licenses/pandas/9bc59dfb5518a0bf9fdac69028fb3c85b869a9e1
/usr/share/package-licenses/pandas/9d84be01def522d7ac0016e7ccf20bf0f56c74c4
/usr/share/package-licenses/pandas/a0386bf16298550823fe867827ba493445658bcc
/usr/share/package-licenses/pandas/c6e195f9aa30cc9b675d1612ca4fb7f74111bd35
/usr/share/package-licenses/pandas/f3b34c666d9f93071f6dbeeea6f8daefc2258e90

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
