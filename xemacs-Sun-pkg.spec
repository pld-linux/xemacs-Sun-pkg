### Comment
# This file is modified automatically by 'xemacs-adapter' script
# from PLD-project CVS repository: cvs.pld.org.pl, module SPECS
# For more details see comments in this script
### EndComment

Summary: 	Support for Sparcworks.
Summary(pl):	Support for Sparcworks.

Name:    	xemacs-Sun-pkg
%define 	srcname	Sun
Version: 	1.11
Release:	1

### Preamble
Copyright:	GPL
Group:    	Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
URL:      	http://www.xemacs.org
Source:   	ftp://ftp.xemacs.org/packages/%{srcname}-%{version}-pkg.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires: 	xemacs
Requires: 	xemacs-cc-mode-pkg
Requires: 	xemacs-base-pkg
### EndPreamble

%description


%description -l pl 


%package el
Summary: 	Support for Sparcworks. This package contains .el files
Summary(pl):	Support for Sparcworks. Pliki ¿ród³owe .el

### ElPreamble
Group:    	Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires: 	%{name} = %{version}
### EndElPreamble


%description el
.el source files -- not necessary to run XEmacs

%description el -l pl
Pliki ¼ród³owe procedur w eLispie do XEmacsa.


### Main
%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
### EndMain

### PrePost
### EndPrePost

### Files
%files
%{_datadir}/xemacs-packages/lisp/*
### EndFiles
