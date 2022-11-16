Name:		texlive-mathpartir
Version:	39864
Release:	1
Summary:	Typesetting sequences of math formulas, e.g. type inference rules
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mathpartir
License:	gpl2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathpartir.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathpartir.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathpartir.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides macros for typesetting math formulas in
mixed horizontal and vertical mode, automatically as best fit.
It provides an environment mathpar that behaves much as a loose
centered paragraph where words are math formulas, and spaces
between them are larger and adjustable. It also provides a
macro \inferrule for typeseting fractions where both the
numerator and denominator may be sequences of formulas that
will be also typeset in a similar way. It can typically be used
for typeseting sets of type inference rules or typing
derivations. A macro inferrule for typesetting type inference
rules.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/mathpartir
%{_texmfdistdir}/tex/latex/mathpartir
%doc %{_texmfdistdir}/doc/latex/mathpartir

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
