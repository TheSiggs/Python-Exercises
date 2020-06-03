 h := 1 /* initialization of the pivot row */
 k := 1 /* initialization of the pivot column */
 while h ≤ m and k ≤ n
   /* Find the k-th pivot: */
   i_max := argmax (i = h ... m, abs(A[i, k]))
   if A[i_max, k] = 0
     /* No pivot in this column, pass to next column */
     k := k+1
   else
      swap rows(h, i_max)
      /* Do for all rows below pivot: */
      for i = h + 1 ... m:
         f := A[i, k] / A[h, k]
         /* Fill with zeros the lower part of pivot column: */
         A[i, k]  := 0
         /* Do for all remaining elements in current row: */
         for j = k + 1 ... n:
            A[i, j] := A[i, j] - A[h, j] * f
      /* Increase pivot row and column */
      h := h+1 
      k := k+1