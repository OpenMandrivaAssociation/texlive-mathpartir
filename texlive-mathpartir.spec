%global tl_name mathpartir
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3.2
Release:	%{tl_revision}.1
Summary:	Typesetting sequences of math formulas, e.g. type inference rules
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mathpartir
License:	gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathpartir.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathpartir.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathpartir.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides macros for typesetting math formulas in mixed
horizontal and vertical mode, automatically as best fit. It provides an
environment mathpar that behaves much as a loose centered paragraph
where words are math formulas, and spaces between them are larger and
adjustable. It also provides a macro \inferrule for typesetting
fractions where both the numerator and denominator may be sequences of
formulas that will be also typeset in a similar way. It can typically be
used for typesetting sets of type inference rules or typing derivations.
A macro inferrule for typesetting type inference rules.

