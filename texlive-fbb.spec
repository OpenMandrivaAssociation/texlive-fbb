%global tl_name fbb
%global tl_revision 77682
%global tl_version 1.16

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	A free Bembo-like font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/fbb
License:	ofl lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fbb.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fbb.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The package provides a Bembo-like font package based on Cardo but with
many modifications, adding Bold Italic, small caps in all styles, six
figure choices in all styles, updated kerning tables, added figure
tables and corrected f-ligatures. Both OpenType and Adobe Type 1
versions are provided; all necessary support files are provided. The
font works well with newtxmath's libertine option.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from fbb:
Map fbb.map
TL_DROPIN_EOF
