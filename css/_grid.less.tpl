
.sgrid_setup(900px, 6, 20px); // set grid ty 6 coulumns
body{
  .sgrid; // apply grid to body
  article{ 
    .row(); // create row
    .equal_col_wrap(); // wrap to make inner colums equal height
    section {
      .col(2); // column 2col wide
      .col_left; // float colums left
      .no_gaps; // remove gaps
      .equal_col(); // set equal height to collums
    }
  }
}  
