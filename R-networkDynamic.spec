%global packname networkDynamic
%global rlibdir %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.4.1
Release:          1
Summary:          Dynamic Extensions for Network Objects
Group:            Sciences/Mathematics
License:          GPLv3
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-network >= 1.7.2 R-statnet.common R-testthat >= 0.7.1
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-network >= 1.7.2 R-statnet.common R-testthat >= 0.7.1

%description
Simple interface routines to facilitate the handling of
network objects with complex intertemporal data.
networkDynamic is a part of the statnet suite of packages for network analysis.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
