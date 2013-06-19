#
%define		_state		stable
%define		orgname		print-manager
%define		qtver		4.8.0

Summary:	K Desktop Environment - print manager
Name:		kde4-print-manager
Version:	4.10.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	d322cff87bd8914de116e656d724244e
URL:		http://www.kde.org/
BuildRequires:	automoc4
BuildRequires:	kde4-kdebase-devel >= %{version}
BuildRequires:	qt4-build
Requires:	kde4-kdebase-workspace >= %{version}
Obsoletes:	kde4-kdeutils-printer-applet
Obsoletes:	kde4-printer-applet
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Printing management for KDE.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

#%find_lang %{orgname} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

#%files -f %{orgname}.lang
%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkcupslib.so
%attr(755,root,root) %{_libdir}/kde4/libexec/configure-printer
%attr(755,root,root) %{_libdir}/kde4/libexec/add-printer
%attr(755,root,root) %{_libdir}/kde4/libexec/print-queue
%attr(755,root,root) %{_libdir}/kde4/kcm_printer_manager.so
%attr(755,root,root) %{_libdir}/kde4/kded_printmanager.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_printjobs.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_printers.so
%{_datadir}/apps/plasma/plasmoids/printmanager
%{_datadir}/apps/plasma/services/org.kde.printjobs.operations
%{_datadir}/apps/plasma/services/org.kde.printers.operations
%{_datadir}/apps/printmanager
%{_datadir}/kde4/services/plasma-applet-printmanager.desktop
%{_datadir}/kde4/services/kcm_printer_manager.desktop
%{_datadir}/kde4/services/kded/printmanager.desktop
%{_datadir}/kde4/services/plasma-engine-printjobs.desktop
%{_datadir}/kde4/services/plasma-engine-printers.desktop
%{_datadir}/dbus-1/services/org.kde.ConfigurePrinter.service
%{_datadir}/dbus-1/services/org.kde.AddPrinter.service
%{_datadir}/dbus-1/services/org.kde.PrintQueue.service
