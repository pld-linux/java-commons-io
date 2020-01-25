#
# Conditional build:
%bcond_without	javadoc		# don't build javadoc
%bcond_with	tests		# run tests (takes long time)

%define		srcname	commons-io
Summary:	Commons IO component for Java servlets
Summary(pl.UTF-8):	Komponent Commons IO dla serwletów Javy
Name:		java-commons-io
Version:	1.4
Release:	3
License:	Apache v2.0
Group:		Libraries/Java
Source0:	http://www.apache.org/dist/commons/io/source/commons-io-%{version}-src.tar.gz
# Source0-md5:	24b228f2d0c40ffed9204cdab015bccf
URL:		http://commons.apache.org/io/
BuildRequires:	ant
%{?with_tests:BuildRequires:	ant-junit >= 1.5}
BuildRequires:	jdk
BuildRequires:	jpackage-utils
%{?with_tests:BuildRequires:	junit >= 3.8.1}
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
Obsoletes:	jakarta-commons-io
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
Obsoletes:	jakarta-commons-io-javadoc

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
%ant jar %{?with_javadoc:javadoc}

%if %{with tests}
JUNITJAR=$(find-jar junit)
%ant -Djunit.jar=$JUNITJAR test
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

cp -a target/commons-io-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -sf commons-io-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-io.jar

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -a target/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
%endif
