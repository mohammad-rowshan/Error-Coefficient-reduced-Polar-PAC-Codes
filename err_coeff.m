function [dmin, A_dmin] = err_coeff(I,N)
  d = min(sum(dec2bin(I)-'0',2));
  dmin = 2ˆd; n = log2(N); A_dmin = 0;
  B = find(sum(dec2bin(I)-'0',2)==d);
  for i = B'
    Ki_size = n - d;
    for x = find(dec2bin(I(i),n)-'0'==1)
      ii = dec2bin(bitxor(N-1,I(i)))-'0';
      Ki_size = Ki_size + sum(ii(1:x-1));
    end
    A_dmin = A_dmin + 2ˆKi_size;
  end
end
