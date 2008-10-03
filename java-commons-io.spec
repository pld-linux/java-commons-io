#
# Conditional build:
%bcond_without	javadoc		# don't build javadoc

%include	/usr/lib/rpm/macros.java
Summary:	Jakarta Commons IO component for Java servlets
Summary(pl.UTF-8):	Komponent Jakarta Commons IO dla serwletów Javy
Name:		jakarta-commons-io
Version:	1.4
Release:	1
License:	Apache v2.0
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/commons/io/source/commons-io-%{version}-src.tar.gz
# Source0-md5:	24b228f2d0c40ffed9204cdab015bccf
URL:		http://commons.apache.org/io/
BuildRequires:	ant-junit >= 1.5
BuildRequires:	jakarta-servletapi >= 2.3
BuildRequires:	jpackage-utils
BuildRequires:	junit >= 3.8.1
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
Requires:	jre
Obsoletes:	jakarta-commons-io-doc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Commons IO is a library of utilities to assist with developing I/O
functionality.

%description -l pl.UTF-8
Commons IO to biblioteka narzędzi pomagających przy rozwijaniu
funkcjonalności I/O.

%package javadoc
Summary:	Online manual for Commons IO
Summary(pl.UTF-8):	Dokumentacja online do Commons IO
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Documentation for Commons IO.

%description javadoc -l pl.UTF-8
Dokumentacja do Commons IO.

%description javadoc -l fr.UTF-8
Javadoc pour Commons IO.

%prep
%setup -q -n commons-io-%{version}-src

%build
# for tests
CLASSPATH=$(build-classpath servlet junit)
%ant jar %{?with_javadoc:javadoc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

cp -a target/commons-io-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -sf commons-io-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-io.jar

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a target/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
%endif
