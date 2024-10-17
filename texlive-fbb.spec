Name:		texlive-fbb
Version:	55728
Release:	2
Summary:	A free Bembo-like font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/fbb
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fbb.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fbb.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a Bembo-like font package based on Cardo
but with many modifications, adding Bold Italic, small caps in
all styles, six figure choices in all styles, updated kerning
tables, added figure tables and corrected f-ligatures. Both
OpenType and Adobe Type 1 versions are provided; all necessary
support files are provided. The font works well with
newtxmath's libertine option.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/fbb
%{_texmfdistdir}/fonts/map/dvips/fbb
%{_texmfdistdir}/fonts/opentype/public/fbb
%{_texmfdistdir}/fonts/tfm/public/fbb
%{_texmfdistdir}/fonts/type1/public/fbb
%{_texmfdistdir}/fonts/vf/public/fbb
%{_texmfdistdir}/tex/latex/fbb
%doc %{_texmfdistdir}/doc/fonts/fbb

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
