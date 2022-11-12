Name:		texlive-ean13isbn
Version:	57514
Release:	1
Summary:	Print EAN13 for ISBN
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ean13isbn
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ean13isbn.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ean13isbn.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the means to typeset ISBN codes with EAN-
13; it uses the (generic) package ean13.tex to typeset the
actual barcode.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ean13isbn/ean13isbn.sty
%doc %{_texmfdistdir}/doc/latex/ean13isbn/License.txt
%doc %{_texmfdistdir}/doc/latex/ean13isbn/README
%doc %{_texmfdistdir}/doc/latex/ean13isbn/ean13isbn.pdf
%doc %{_texmfdistdir}/doc/latex/ean13isbn/ean13isbn.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
