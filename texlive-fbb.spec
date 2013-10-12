# revision 31869
# category Package
# catalog-ctan /fonts/fbb
# catalog-date 2013-10-09 07:11:28 +0200
# catalog-license ofl
# catalog-version 0.93
Name:		texlive-fbb
Version:	0.93
Release:	1
Summary:	A free Bembo-like font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/fbb
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fbb.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fbb.doc.tar.xz
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
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_2qutta.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_2xteu2.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_3gezys.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_3jy3vu.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_3pafo2.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_3q7523.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_3szmnl.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_3t72qi.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_47nzug.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_4eykqf.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_4fm2lh.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_4phrex.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_54mbhb.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_5g5giq.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_5kfdlm.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_5yuftp.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_646rxv.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_6jg7cq.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_7ftbhc.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_bbqv4h.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_bjcd27.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_bwe6jm.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_cglacz.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_ciz6qs.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_dfjaoq.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_dfzymh.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_dli7xt.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_do4apa.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_dppuce.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_dzuzoo.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_eaddwb.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_eie4y7.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_fefik6.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_fpos6t.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_gia3f7.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_gti7xr.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_h4yzgv.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_hjhis6.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_hyfmfg.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_icb62t.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_ikoi5j.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_inh3kf.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_iqrulf.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_j2glsr.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_jeovrq.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_k4t5oa.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_ksln4y.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_lahflm.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_ms7h4m.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_nakqlt.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_p2khiw.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_p6sgcp.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_pjzzzk.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_pqcug3.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_qxzlqe.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_qyua2i.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_r5yodg.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_symdpm.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_syrpbc.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_thr2ik.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_tizue6.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_tpadeo.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_u3ego5.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_uqncc5.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_vkojsi.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_vvs2t7.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_w6cgkc.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_wmfgc4.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_wmijbz.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_xmsf7g.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_xoiwwh.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_yr6epv.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_zac64m.enc
%{_texmfdistdir}/fonts/enc/dvips/fbb/fbb_zxsywv.enc
%{_texmfdistdir}/fonts/map/dvips/fbb/fbb.map
%{_texmfdistdir}/fonts/opentype/public/fbb/fbb-Bold.otf
%{_texmfdistdir}/fonts/opentype/public/fbb/fbb-BoldItalic.otf
%{_texmfdistdir}/fonts/opentype/public/fbb/fbb-Italic.otf
%{_texmfdistdir}/fonts/opentype/public/fbb/fbb-Regular.otf
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Bold-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-BoldItalic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Italic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/fbb/fbb-Regular-tosf-ts1.tfm
%{_texmfdistdir}/fonts/type1/public/fbb/fbb-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/fbb/fbb-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/public/fbb/fbb-Italic.pfb
%{_texmfdistdir}/fonts/type1/public/fbb/fbb-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Bold-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Bold-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Bold-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Bold-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Bold-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Bold-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Bold-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Bold-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Bold-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Bold-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Bold-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Bold-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Bold-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Bold-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Bold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Bold-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Bold-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Bold-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Bold-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Bold-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Bold-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Bold-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Bold-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Bold-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-BoldItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-BoldItalic-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-BoldItalic-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-BoldItalic-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-BoldItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-BoldItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-BoldItalic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-BoldItalic-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-BoldItalic-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-BoldItalic-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-BoldItalic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-BoldItalic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-BoldItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-BoldItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-BoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-BoldItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-BoldItalic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-BoldItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-BoldItalic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-BoldItalic-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-BoldItalic-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-BoldItalic-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-BoldItalic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-BoldItalic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Italic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Italic-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Italic-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Italic-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Italic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Italic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Italic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Italic-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Italic-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Italic-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Italic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Italic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Italic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Italic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Italic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Italic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Italic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Italic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Italic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Italic-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Italic-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Italic-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Italic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Italic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Regular-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Regular-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Regular-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Regular-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Regular-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Regular-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Regular-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Regular-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Regular-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Regular-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Regular-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Regular-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Regular-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Regular-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Regular-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Regular-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Regular-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Regular-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Regular-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Regular-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Regular-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Regular-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Regular-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Regular-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Regular-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/fbb/fbb-Regular-tosf-ts1.vf
%{_texmfdistdir}/tex/latex/fbb/LY1fbb-LF.fd
%{_texmfdistdir}/tex/latex/fbb/LY1fbb-OsF.fd
%{_texmfdistdir}/tex/latex/fbb/LY1fbb-Sup.fd
%{_texmfdistdir}/tex/latex/fbb/LY1fbb-TLF.fd
%{_texmfdistdir}/tex/latex/fbb/LY1fbb-TOsF.fd
%{_texmfdistdir}/tex/latex/fbb/OT1fbb-LF.fd
%{_texmfdistdir}/tex/latex/fbb/OT1fbb-OsF.fd
%{_texmfdistdir}/tex/latex/fbb/OT1fbb-Sup.fd
%{_texmfdistdir}/tex/latex/fbb/OT1fbb-TLF.fd
%{_texmfdistdir}/tex/latex/fbb/OT1fbb-TOsF.fd
%{_texmfdistdir}/tex/latex/fbb/T1fbb-LF.fd
%{_texmfdistdir}/tex/latex/fbb/T1fbb-OsF.fd
%{_texmfdistdir}/tex/latex/fbb/T1fbb-Sup.fd
%{_texmfdistdir}/tex/latex/fbb/T1fbb-TLF.fd
%{_texmfdistdir}/tex/latex/fbb/T1fbb-TOsF.fd
%{_texmfdistdir}/tex/latex/fbb/TS1fbb-LF.fd
%{_texmfdistdir}/tex/latex/fbb/TS1fbb-OsF.fd
%{_texmfdistdir}/tex/latex/fbb/TS1fbb-TLF.fd
%{_texmfdistdir}/tex/latex/fbb/TS1fbb-TOsF.fd
%{_texmfdistdir}/tex/latex/fbb/fbb.sty
%doc %{_texmfdistdir}/doc/fonts/fbb/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/fbb/README
%doc %{_texmfdistdir}/doc/fonts/fbb/fbb-doc.pdf
%doc %{_texmfdistdir}/doc/fonts/fbb/fbb-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}