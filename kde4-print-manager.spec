#
%define		_state		stable
%define		orgname		print-manager
%define		qtver		4.8.0
%define		kdeworkspacever	4.11.0

Summary:	K Desktop Environment - print manager
Name:		kde4-print-manager
Version:	4.14.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	003c56957e141d8912f0a90567a29cfe
URL:		http://www.kde.org/
BuildRequires:	automoc4
BuildRequires:	cups-devel
BuildRequires:	kde4-kdebase-devel >= %{version}
BuildRequires:	qt4-build
Requires:	kde4-kdebase-workspace >= %{kdeworkspacever}
Obsoletes:	kde4-kdeutils-print-manager
Obsoletes:	kde4-printer-manager
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Printer Applet is a system tray utility that shows current print jobs,
shows printer warnings and errors.

%description -l pl.UTF-8
Printer Applet to narzedzie zasobnika systemowego, ktore pokazuje
aktualne zadania drukarki, ostrzezenia i bledy.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DINSTALL_PRINTER_APPLET=TRUE \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kde-add-printer
%attr(755,root,root) %{_bindir}/kde-print-queue
%dir %{_libdir}/kde4/imports/org/kde/printmanager
%{_libdir}/kde4/imports/org/kde/printmanager/qmldir
%attr(755,root,root) %{_libdir}/kde4/imports/org/kde/printmanager/libprintmanager.so
%attr(755,root,root) %{_libdir}/kde4/kcm_printer_manager.so
%attr(755,root,root) %{_libdir}/kde4/kded_printmanager.so
%attr(755,root,root) %{_libdir}/kde4/libexec/configure-printer
#%attr(755,root,root) %{_libdir}/kde4/plugins/designer/printmanagerwidget.so
%attr(755,root,root) %{_libdir}/libkcupslib.so
%{_datadir}/apps/plasma/plasmoids/org.kde.printmanager
%{_datadir}/apps/printmanager
%{_datadir}/dbus-1/services/org.kde.ConfigurePrinter.service
%{_datadir}/kde4/services/kcm_printer_manager.desktop
%{_datadir}/kde4/services/kded/printmanager.desktop
%{_datadir}/kde4/services/plasma-applet-printmanager.desktop
