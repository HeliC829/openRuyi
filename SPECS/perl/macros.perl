# macros.perl file
# macros for perl module building. handle with care.

# Useful perl macros
#
%perl_sitearch   %(eval "`%{__perl} -V:installsitearch`"; echo $installsitearch)
%perl_sitelib    %(eval "`%{__perl} -V:installsitelib`"; echo $installsitelib)
%perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%perl_vendorlib  %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%perl_archlib    %(eval "`%{__perl} -V:installarchlib`"; echo $installarchlib)
%perl_privlib    %(eval "`%{__perl} -V:installprivlib`"; echo $installprivlib)

%perl_testdir   %{_libexecdir}/perl5-tests
%cpan_dist_name %(eval echo %{name} | %{__sed} -e 's/^perl-//')

%perl_version           %(perl -V:version | sed "s!.*='!!;s!'.*!!")
%perl_man1ext           %(perl -V:man1ext | sed "s!.*='!!;s!'.*!!")
%perl_man3ext           %(perl -V:man3ext | sed "s!.*='!!;s!'.*!!")
%perl_man1dir           %(perl -V:man1dir | sed "s!.*='!!;s!'.*!!")
%perl_man3dir           %(perl -V:man3dir | sed "s!.*='!!;s!'.*!!")
%perl_installman1dir    %(perl -V:installman1dir | sed "s!.*='!!;s!'.*!!")
%perl_installman3dir    %(perl -V:installman3dir | sed "s!.*='!!;s!'.*!!")
%perl_installarchlib    %(perl -V:installarchlib | sed "s!.*='!!;s!'.*!!")
%perl_prefix            %{buildroot}

%fix_shbang_line() \
TMPHEAD=`mktemp`\
TMPBODY=`mktemp`\
for file in %* ; do \
    head -1 $file > $TMPHEAD\
    tail -n +2 $file > $TMPBODY\
    %{__perl} -pi -e '$f = /^#!/ ? "" : "#!%{__perl}$/"; $_="$f$_"' $TMPHEAD\
    cat $TMPHEAD $TMPBODY > $file\
done\
%{__perl} -MExtUtils::MakeMaker -e "ExtUtils::MM_Unix->fixin(qw{%*})"\
%{__rm} $TMPHEAD $TMPBODY\
%{nil}

%perl_requires() \
Requires: perl(:MODULE_COMPAT_%{perl_version})

%libperl_requires() \
Requires: perl = %{perl_version}

%perl_make_install make DESTDIR=$RPM_BUILD_ROOT install_vendor
%perl_process_packlist(n:) \
  if test -n "$RPM_BUILD_ROOT" -a -d $RPM_BUILD_ROOT%perl_vendorarch/auto; then \
    find $RPM_BUILD_ROOT%perl_vendorarch/auto -name .packlist -print0 | xargs -0 -r rm \
    if [ %{_target_cpu} == noarch ]; then \
      find $RPM_BUILD_ROOT%perl_vendorarch/auto -depth -type d -print0 | xargs -0 -r rmdir \
    fi \
  fi \
  rm -f $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod \
  %nil

# macro: perl_gen_filelist
# do the rpmlint happy filelist generation
# with %dir in front of directories
#
%perl_gen_filelist(n)\
FILES=%{name}.files\
# fgen_dir func\
# IN: dir\
fgen_dir(){\
%{__cat} >> $FILES << EOF\
%dir ${1}\
EOF\
}\
# fgen_file func\
# IN: file\
fgen_file(){\
%{__cat} >> $FILES << EOF\
${1}\
EOF\
}\
# handle %{perl_vendorarch} (arch-specific vendor dir) if it exists\
if [ -d ${RPM_BUILD_ROOT}%{perl_vendorarch} ]; then\
  # check for files in %{perl_vendorarch}\
  RES=`find ${RPM_BUILD_ROOT}%{perl_vendorarch} -maxdepth 1 -type f`\
  if [ -n "$RES" ]; then\
    for file in $RES; do\
      fgen_file "%{perl_vendorarch}/$(basename ${file})"\
    done\
  fi\
  \
  # get all dirs into array\
  base_dir="${RPM_BUILD_ROOT}%{perl_vendorarch}/"\
  all_dir=()\
  for dir in `find ${base_dir} -type d | sort`; do\
    if [ "$dir" = "${base_dir}" ]; then\
      continue\
    else\
      el=${dir#$base_dir}\
      all_dir=(${all_dir[@]} $el)\
    fi\
  done\
  \
  # build filelist\
  for i in ${all_dir[@]}; do\
    # do not add "dir {perl_vendorarch/arch}/auto", included in perl package\
    if [ "${i}" = "auto" ]; then\
      continue\
    fi\
    if [ "%{perl_vendorarch}/${i}" = "%{perl_vendorarch}/auto" ]; then\
      continue\
    else\
      if [ -d ${base_dir}/${i} ]; then\
        if [ "%{perl_vendorarch}/${i}" != "%{perl_vendorarch}" ]; then\
          fgen_dir "%{perl_vendorarch}/${i}"\
        fi\
        RES=`find "${base_dir}/${i}" -maxdepth 1 -type f`\
        for file in $RES; do\
          fgen_file "%{perl_vendorarch}/${i}/$(basename ${file})"\
        done\
      fi\
    fi\
  done\
fi\
\
# handle %{perl_vendorlib} (pure-perl vendor dir) if it exists\
if [ -d ${RPM_BUILD_ROOT}%{perl_vendorlib} ]; then\
  # check for files in %{perl_vendorlib}\
  RES=`find ${RPM_BUILD_ROOT}%{perl_vendorlib} -maxdepth 1 -type f`\
  if [ -n "$RES" ]; then\
    for file in $RES; do\
      fgen_file "%{perl_vendorlib}/$(basename ${file})"\
    done\
  fi\
  \
  # get all dirs into array\
  base_dir="${RPM_BUILD_ROOT}%{perl_vendorlib}/"\
  all_dir=()\
  for dir in `find ${base_dir} -type d | sort`; do\
    if [ "$dir" = "${base_dir}" ]; then\
      continue\
    else\
      el=${dir#$base_dir}\
      all_dir=(${all_dir[@]} $el)\
    fi\
  done\
  \
  # build filelist\
  for i in ${all_dir[@]}; do\
    # do not add auto directories either\
    if [ "${i}" = "auto" ]; then\
      continue\
    fi\
    if [ "%{perl_vendorlib}/${i}" = "%{perl_vendorlib}/auto" ]; then\
      continue\
    else\
      if [ -d ${base_dir}/${i} ]; then\
        if [ "%{perl_vendorlib}/${i}" != "%{perl_vendorlib}" ]; then\
          fgen_dir "%{perl_vendorlib}/${i}"\
        fi\
        RES=`find "${base_dir}/${i}" -maxdepth 1 -type f`\
        for file in $RES; do\
          fgen_file "%{perl_vendorlib}/${i}/$(basename ${file})"\
        done\
      fi\
    fi\
  done\
fi\
# add man pages\
# if exist :)\
if [ -d "${RPM_BUILD_ROOT}%{_mandir}" ]; then\
EXT="%{perl_man3ext}"\
for file in `cd "${RPM_BUILD_ROOT}%{_mandir}" && find . -type f -name "*${EXT}*"`; do \
   new="${file/${EXT}/${EXT}c}" \
   src="${RPM_BUILD_ROOT}%{_mandir}/$file" \
   dst="${RPM_BUILD_ROOT}%{_mandir}/$new" \
   if [ -e "$src" ]; then \
     mv "$src" "$dst" \
   elif [ -e "$src.gz" ]; then \
     mv "$src.gz" "$dst.gz" \
   fi \
done \
fgen_file "%{_mandir}/man?/*"\
fi\
\
# add packlist file\
# generated fom perllocal.pod\
if [ -f "${RPM_BUILD_ROOT}/var/adm/perl-modules/%{name}" ]; then\
  fgen_file "/var/adm/perl-modules/%{name}"\
fi\
\
# check for files in %{_bindir}\
if [ -d ${RPM_BUILD_ROOT}%{_bindir} ]; then\
  RES=`find "${RPM_BUILD_ROOT}%{_bindir}" -maxdepth 1 -type f`\
  if [ -n "$RES" ]; then\
    for file in $RES; do\
      fgen_file "%{_bindir}/$(basename ${file})"\
    done\
  fi\
fi
