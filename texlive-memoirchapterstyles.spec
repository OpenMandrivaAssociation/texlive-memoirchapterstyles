%global tl_name memoirchapterstyles
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.7e
Release:	%{tl_revision}.1
Summary:	Chapter styles in memoir class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/latex-samples/MemoirChapStyles
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/memoirchapterstyles.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/memoirchapterstyles.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A showcase of chapter styles available to users of memoir: the six
provided in the class itself, plus many from elsewhere (by the present
author and others). The package's resources apply only to memoir, but
the package draws from a number of sources relating to standard classes,
including the fncychap package, and Vincent Zoonekynd's tutorial on
headings.

