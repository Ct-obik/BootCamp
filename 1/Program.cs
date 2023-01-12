// дан массив и найти максимум из 3 подряд чисел этого массива

int size = 10;
int m = 3;
int[] array = Enumerable.Range(1, size)
                        .Select(item => Random.Shared.Next(10)) // случайные числа от 0 до 10
                        .ToArray();

Console.WriteLine(string.Join(' ', array));

int max = 0;
for (int j = 0; j < m; j++) max += array[j];
int t = max;
for (int i = 1; i < array.Length - m; i++)
{
    t = t - array[i - 1] + array[i + (m - 1)];
    if (t > max) max = t;
}
Console.WriteLine(max);