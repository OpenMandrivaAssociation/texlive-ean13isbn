# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/ean13isbn
# catalog-date 2008-08-19 08:58:40 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-ean13isbn
Version:	20080819
Release:	1
Summary:	Print EAN13 for ISBN
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ean13isbn
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ean13isbn.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ean13isbn.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides the means to typeset ISBN codes with EAN-
13; it uses the (generic) package ean13.tex to typeset the
actual barcode.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ean13isbn/ean13isbn.sty
%doc %{_texmfdistdir}/doc/latex/ean13isbn/License.txt
%doc %{_texmfdistdir}/doc/latex/ean13isbn/README
%doc %{_texmfdistdir}/doc/latex/ean13isbn/ean13isbn.pdf
%doc %{_texmfdistdir}/doc/latex/ean13isbn/ean13isbn.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
