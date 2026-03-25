public class RomanNumerals {
  
  public static String toRoman(int n) {
    String[] ones = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
    String[] tens = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
    String[] cents = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
    String[] mils = {"", "M", "MM", "MMM"};
    return mils[n/1000] + cents[n%1000/100] + tens[n%100/10] + ones[n%10];
  }
  
  public static int fromRoman(String romanumeral) {
    int output = 0;
    String romanNumeral = romanumeral;
    String[] ones = {"IX" ,"VIII" ,"VII" ,"VI" ,"V" ,"IV" ,"III" ,"II" ,"I"};
    for(int x = 0; x < ones.length; x++){
      if(romanNumeral.contains(ones[x])){
        if(romanNumeral.contains("IV")){
          output += 4;
        }
        else{
          output += 9 - x;
        }
        romanNumeral = romanNumeral.substring(0,romanNumeral.length()-ones[x].length());
        break;
      }
    }
    String[] tens = {"XC", "LXXX", "LXX", "LX", "L", "XL", "XXX", "XX", "X"};
    for(int x = 0; x < tens.length; x++){
      if(romanNumeral.contains(tens[x])){
        if(romanNumeral.contains("XL")){
          output += 40;
        }
        else{
          output += 90 - x*10;
        }
        romanNumeral = romanNumeral.substring(0,romanNumeral.length()-tens[x].length());
        break;
      }
    }
    String[] cents = {"CM", "DCCC", "DCC", "DC", "D", "CD", "CCC", "CC", "C"};
    for(int x = 0; x < cents.length; x++){
      if(romanNumeral.contains(cents[x])){
        if(romanNumeral.contains("CD")){
          output += 400;
        }
        else{
          output += 900 - x*100;
        }
        romanNumeral = romanNumeral.substring(0,romanNumeral.length()-cents[x].length());
        break;
      }
    }
    String[] mils = {"MMM", "MM", "M"};
    for(int x = 0; x < mils.length; x++){
      if(romanNumeral.contains(mils[x])){
        output += 3000 - x*1000;
        break;
      }
    }
    
    return output;
  }
}
