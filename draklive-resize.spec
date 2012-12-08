%define name draklive-resize
%define version 0.18.2
%define release %mkrel 3
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
%find_lang %name

%clean
rm -rf %buildroot

%files -f %{name}.lang
%defattr(-,root,root)
%doc NEWS
%_sbindir/%name
%_sysconfdir/X11/xsetup.d/??%{name}.xsetup
%_iconsdir/*.png




%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.18.2-3mdv2011.0
+ Revision: 663857
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.18.2-2mdv2011.0
+ Revision: 604821
- rebuild

* Wed May 26 2010 Christophe Fergeau <cfergeau@mandriva.com> 0.18.2-1mdv2010.1
+ Revision: 546252
- 0.18.2
- translation updates

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.18.1-3mdv2010.1
+ Revision: 522508
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.18.1-2mdv2010.0
+ Revision: 413382
- rebuild

* Wed Apr 15 2009 Thierry Vignaud <tv@mandriva.org> 0.18.1-1mdv2009.1
+ Revision: 367389
- updated translation

* Mon Mar 30 2009 Thierry Vignaud <tv@mandriva.org> 0.18-1mdv2009.1
+ Revision: 362297
- updated translation

* Fri Nov 21 2008 Olivier Blin <oblin@mandriva.com> 0.17-1mdv2009.1
+ Revision: 305405
- 0.17
- fix crash

* Wed Nov 19 2008 Olivier Blin <oblin@mandriva.com> 0.16-1mdv2009.1
+ Revision: 304422
- 0.16
- set wm hints if needed (like dialog)

* Tue Nov 18 2008 Olivier Blin <oblin@mandriva.com> 0.15-1mdv2009.1
+ Revision: 304279
- 0.15
- detect unionfs v1 and use proper options

* Mon Sep 22 2008 Thierry Vignaud <tv@mandriva.org> 0.14-1mdv2009.0
+ Revision: 286977
- updated translation

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 0.13-2mdv2009.0
+ Revision: 264419
- rebuild early 2009.0 package (before pixel changes)

* Fri May 30 2008 Olivier Blin <oblin@mandriva.com> 0.13-1mdv2009.0
+ Revision: 213447
- 0.13
- do not use unionctl but remount commands instead (for unionfs 2.x)
- updated translations

* Thu Apr 03 2008 Thierry Vignaud <tv@mandriva.org> 0.12-2mdv2008.1
+ Revision: 192087
- updated translation

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.11-2mdv2008.1
+ Revision: 149257
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Oct 03 2007 Thierry Vignaud <tv@mandriva.org> 0.11-1mdv2008.0
+ Revision: 95061
- updated translation

* Mon Oct 01 2007 Thierry Vignaud <tv@mandriva.org> 0.10-1mdv2008.0
+ Revision: 94273
- updated translation

* Thu Sep 27 2007 Thierry Vignaud <tv@mandriva.org> 0.9-1mdv2008.0
+ Revision: 93359
- updated translations
- fix building with translations
- updated translations


* Tue Mar 06 2007 Olivier Blin <oblin@mandriva.com> 0.7-1mdv2007.0
+ Revision: 133487
- 0.7

* Mon Mar 05 2007 Olivier Blin <oblin@mandriva.com> 0.6-1mdv2007.1
+ Revision: 132942
- 0.6

* Fri Mar 02 2007 Olivier Blin <oblin@mandriva.com> 0.5-1mdv2007.1
+ Revision: 131082
- 0.5

* Wed Feb 28 2007 Olivier Blin <oblin@mandriva.com> 0.4-1mdv2007.1
+ Revision: 127292
- 0.4

* Tue Feb 27 2007 Olivier Blin <oblin@mandriva.com> 0.3-1mdv2007.1
+ Revision: 126820
- 0.3

* Mon Feb 26 2007 Olivier Blin <oblin@mandriva.com> 0.2-1mdv2007.1
+ Revision: 125890
- 0.2

* Fri Feb 16 2007 Olivier Blin <oblin@mandriva.com> 0.1-1mdv2007.1
+ Revision: 121902
- initial draklive-resize release
- Create draklive-resize

