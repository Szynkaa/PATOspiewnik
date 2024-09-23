@default_files                     = ('PATOśpiewnik.tex');
$pdf_mode                          = 5;                      # xelatex
$aux_dir                           = 'aux';
$warnings_as_errors                = 1;
$cleanup_includes_cusdep_generated = 1;

sub dir2tex {
    print $_;
    system("python3 scripts/chapter.py \"$_[0].d\"");
}

add_cus_dep( 'd', 'tex', 0, 'dir2tex' );

my $extra_dir = $aux_dir . '/piosenki';
if (! -d $extra_dir) {
    mkdir $aux_dir;
    mkdir $extra_dir or die "Cannot create";
}
print $extra_dir;
