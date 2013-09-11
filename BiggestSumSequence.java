class BiggestSumSequence {
  public static int BiggestsSumSequence(int[] s){
      // find the first one +num
      int i;
      for ( i = 0; i < s.length-1, i++){
          if (s[i] >=0) break;
      }
      return BiggestSumSequence(i,s.length-1,s);
  }
  // return the sum of the biggest sequence 
  private int BiggestSumSequence(int start, int end, int[] s){
      if (end == 0){
          return 0;
      } else {
          int temp =  sum(end+1,s.length-1, s);
          if (  >=0 ){
              return BiggestSumSequence(start, end-1, s) + 
          } else {
               
          }
      }
  }
}
