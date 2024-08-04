@default_files                     = ('PATOśpiewnik.tex');
$pdf_mode                          = 5;                      # xelatex
$aux_dir                           = 'aux';
$warnings_as_errors                = 1;
$cleanup_includes_cusdep_generated = 1;

sub song2tex {
    print $_;
    system("python3 scripts/song2tex.py \"$_[0].song\"  \"$_[0].tex\"");
}

add_cus_dep( 'song', 'tex', 0, 'song2tex' );

sub dir2tex {
    print $_;
    system("python3 scripts/chapter.py \"$_[0].d\"");
}

add_cus_dep( 'd', 'tex', 0, 'dir2tex' );
