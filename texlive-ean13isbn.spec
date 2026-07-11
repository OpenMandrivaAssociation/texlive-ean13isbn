%global tl_name ean13isbn
%global tl_revision 57514

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Print EAN13 for ISBN
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ean13isbn
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ean13isbn.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ean13isbn.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the means to typeset ISBN codes with EAN-13; it
uses the (generic) package ean13.tex to typeset the actual barcode.

