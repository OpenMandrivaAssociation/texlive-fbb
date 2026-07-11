%global tl_name fbb
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.16
Release:	%{tl_revision}.1
Summary:	A free Bembo-like font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/fbb
License:	ofl lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fbb.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fbb.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a Bembo-like font package based on Cardo but with
many modifications, adding Bold Italic, small caps in all styles, six
figure choices in all styles, updated kerning tables, added figure
tables and corrected f-ligatures. Both OpenType and Adobe Type 1
versions are provided; all necessary support files are provided. The
font works well with newtxmath's libertine option.

