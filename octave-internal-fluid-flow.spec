%global octpkg internal-fluid-flow

Summary:	A toolbox for internal fluid flow for GNU Octave
Name:		octave-internal-fluid-flow
Version:	0.3.2
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://github.com/aumpierre-unb/Internal-Fluid-Flow-for-GNU-Octave
Source0:	https://github.com/aumpierre-unb/Internal-Fluid-Flow-for-GNU-Octave/archive/v%{version}/internal-fluid-flow-%{version}.tar.gz

BuildRequires:	octave-devel >= 4.2.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
A toolbox for internal fluid flow for GNU Octave.

%files
%license COPYING
%doc NEWS README.md
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n Internal-Fluid-Flow-for-GNU-Octave-%{version}

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

