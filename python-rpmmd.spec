%global srcname pyrpmmd


Name:           python-%{srcname}
Version:        0.1.1
Release:        1
Summary:        Python module for reading rpm-md repo data
License:        GPLv2+
URL:            https://pagure.io/%{srcname}
Source0:        https://releases.pagure.org/%{srcname}/%{srcname}-%{version}.tar.xz
BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python-setuptools
Requires:       python-six

%description 
pyrpmmd is an independent Python module for reading 
rpm-md repository metadata. The code is derived from 
the repomd parsing code from Yum

#%%package     -n python-%%{srcname}
Summary:        Python module for reading rpm-md repo data

%prep
%setup -q -n %{srcname}-%{version}


%build
%{__python} setup.py build


%install
%{__python} setup.py install --skip-build --root %{buildroot}


%files -n python-%{srcname}
%license COPYING
%doc README.md ChangeLog
%{python3_sitelib}/rpmmd/
%{python3_sitelib}/%{srcname}-%{version}*/


