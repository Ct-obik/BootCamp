// Записываем числа в массив и показываем определённое число из массива
Console.WriteLine("ВВедите числа массива:");
int[] array = new int[5];
for (int i = 0; i < 5; i++)
    array[i] = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("[" + string.Join(", ", array) + "]");
Console.WriteLine(array[3]);
// Сложность алгоритма - Онотация
// Это кол-во действий, чтобы узнать конечный результат.
// Для данной программы - О(1)
 
// Ниже таблица, матрица, в которой подряд цифры переумножаются в таблицу и мы задаём, какое число будет
// перемножаться
Console.WriteLine("Введите число для размера таблицы:");
int n = Convert.ToInt32(Console.ReadLine());
int[,] matrix =  new int[n, n];
for (int i = 0; i < n; i++)
{
for (int j = i; j < n; j++)
    {
      matrix[i,j] = (i + 1)*(j + 1);
      matrix[j,i] = (i + 1)*(j + 1);
    }
    Console.WriteLine();
 }
 for (int i = 0; i < n; i++)
 {
    for (int j = 0; j < n; j++)
    {
      Console.Write(matrix[i,j]);
      Console.Write(" ");
    }
    Console.WriteLine();
 }
// выше - О (n^2 / 2)
