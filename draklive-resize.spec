%define iconname	MandrivaOne-resize-icon.png

Summary:	Live system resizing tool
Name:		draklive-resize
Version:	0.18.2
Release:	11
License:	GPLv2
Group:		System/Configuration/Other
Url:		https://svn.mandriva.com/svn/soft/draklive-resize
Source0:	%{name}-%{version}.tar.bz2
BuildArch:      noarch

%description
This tool allows to resize a the system space for live systems.

%prep
%setup -q

%build
%make

%install
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%doc NEWS
%{_sbindir}/%{name}
%{_sysconfdir}/X11/xsetup.d/??%{name}.xsetup
%{_iconsdir}/*.png

