program ZAshita;

{$APPTYPE CONSOLE}

uses
  SysUtils;

const
  MaxRow = 6;
  MaxColumn = 8;

var
  D : array[1..MaxRow,1..MaxColumn] of string;
  ArrayElements : array[1..MaxRow] of string;
  CountRow, CountColumn : integer;
  i,j : integer;
  Str : string;
  k1,k2,k,l : integer;
  A : boolean;

begin
  write('Введите количество строк матрицы: ');
  readln(CountRow);
  write('Введите количество столбцов матрицы: ');
  readln(CountColumn);
//Ввод матрицы
  for i := 1 to CountRow do
    readln(ArrayElements[i]);
  for i := 1 to CountRow do
    Begin
      Str := ArrayElements[i];
      for j := 1 to CountColumn do
        Begin
          D[i,j] := copy(Str,j,1)
        End;
    End;

//Замена символов
          {if (k1 <> -1) and (i = k1) then
            D[i,j] := '#';
          if (k2 <> -1) and (j = k2) then
            D[i,j] := '#';
          if pos(D[i,j],'0123456789') <> 0 then
            Begin
              D[i,j] := '#';
              k1 := i;
              k2 := j;
            End;
  k1 := -1;
  k2 := -1; }
  k := 0;
  for i := 1 to CountRow do
    for j := 1 to CountColumn do
      Begin
        if pos(D[i,j],'0123456789') <> 0 then
          Begin
            k := k + 1;
            ArrayElements[k] := string(i);
          End;
      End;

  for i := 1 to CountRow do
    for j := 1 to CountColumn do
      Begin
      A := False;
        for l := 1 to k do
          if integer(ArrayElements[l]) = i then
            A := True;
      if A = True then
        D[i,j] := '#';
      End;
        
        


//Вывод введенной матрицы
  for i := 1 to CountRow do
    Begin
      for j := 1 to CountColumn do
        write(D[i,j]);
      writeln;
    End;
  readln;
  readln;
end.
