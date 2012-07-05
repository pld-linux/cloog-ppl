Summary:	The Chunky Loop Generator
Summary(pl.UTF-8):	Chunky Loop Generator - generator pętli cząstkowych
Name:		cloog-ppl
Version:	0.15.11
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	ftp://gcc.gnu.org/pub/gcc/infrastructure/%{name}-%{version}.tar.gz
# Source0-md5:	060ae4df6fb8176e021b4d033a6c0b9e
Patch0:		%{name}-info.patch
URL:		http://www.cloog.org/
BuildRequires:	autoconf >= 2.13
BuildRequires:	automake
BuildRequires:	gmp-devel >= 4.1.3
BuildRequires:	gmp-c++-devel >= 4.1.3
BuildRequires:	libtool
BuildRequires:	ppl-devel >= 0.10
BuildRequires:	texinfo >= 4.12
Requires(post):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CLooG is a software which generates loops for scanning Z-polyhedra.
That is, CLooG finds the code or pseudo-code where each integral point
of one or more parametrized polyhedron or parametrized polyhedra union
is reached. CLooG is designed to avoid control overhead and to produce
a very efficient code.

This version is based on Parma Polyhedra Library (ppl).

%description -l pl.UTF-8
CLooG to oprogramowanie generujące pętle do przeszukiwania
Z-wielościanów (Z-polyhedra). Oznacza to, że CLooG znajduje kod lub
pseudokod osiągający każdy punkt całkowity jednego lub większej liczby
sparametryzowanych wielościanów lub sum sparametryzowanych
wielościanów. CLooG jest zaprojektowany z myślą o zapobieganiu
narzutowi na sterowaniu oraz generowaniu bardzo wydajnego kodu.

Ta wersja jest oparta na bibliotece ppl (Parma Polyhedra Library).

%package devel
Summary:	Header files for the ppl based version of Chunky Loop Generator
Summary(pl.UTF-8):	Pliki nagłówkowe opartej na ppl wersji Chunky Loop Generatora
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gmp-devel >= 4.1.3
Requires:	gmp-c++-devel >= 4.1.3
Requires:	ppl-devel >= 0.10

%description devel
The header files for Chunky Loop Generator library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Chunky Loop Generatora.

%package static
Summary:	Static library of ppl based version of Chunky Loop Generator
Summary(pl.UTF-8):	Statyczna biblioteka opartej na ppl wersji Chunky Loop Generatora
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static library of ppl based version of Chunky Loop Generator.

%description static -l pl.UTF-8
Statyczna biblioteka opartej na ppl wersji Chunky Loop Generatora.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-ppl

# Remove the cloog.info in the tarball
# to force the re-generation of a new one
test -f doc/cloog.info && %{__rm} doc/cloog.info

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL="%{__install} -p" \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
/sbin/ldconfig
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
/sbin/ldconfig
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{_bindir}/cloog
%attr(755,root,root) %{_libdir}/libcloog.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcloog.so.0
%{_infodir}/cloog.info*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcloog.so
%{_libdir}/libcloog.la
%{_includedir}/cloog

%files static
%defattr(644,root,root,755)
%{_libdir}/libcloog.a
