%define name draklive-resize
%define version 0.7
%define release %mkrel 1
%define iconname MandrivaOne-resize-icon.png

Summary:	Live system resizing tool
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
License:	GPL
Group:		System/Configuration/Other
Url:		https://svn.mandriva.com/svn/soft/draklive-resize
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:      noarch

%description
This tool allows to resize a the system space for live systems.

%prep
%setup -q

%build
%make

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc NEWS
%_sbindir/%name
%_sysconfdir/X11/xsetup.d/??%{name}.xsetup
%_iconsdir/*.png


