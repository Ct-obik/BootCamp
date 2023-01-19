public static class Sorting
{

    /// <summary>
    /// Сортировка методом выбора
    /// </summary>
    /// <param name="collection">Исходный массив</param>
    /// <returns>Отсортированный массив массив</returns>
    public static int[] SortCounting(this int[] collection)
    {
        int size = collection.Length;
        int max = collection[0];  // находим максимальное число
        for (int i = 1; i < size; i++)
            if (collection[i] > max) max = collection[i]; // 12-14 можно записать в С# так: int max = collectiom.Max();
        int[] counter = new int[max + 1];
        for (int i = 0; i < size; i++)  // Создаём массив с кол-вом повторяющихся чисел массива
            counter[collection[i]]++;
        int index = 0;  // Создаём массив с сортировкой
        for (int i = 0; i < max + 1; i++)
            for (int j = 0; j < counter[i]; j++)
                collection[index++] = i;
        return collection;
    }
}
// Сложность алгоритма:
// При нахождении max, учитывая общее кол-во чисел массива N -> O(N)
// При первом создании массива, учитываем размер массива, то есть N -> O(N)
// При создании массива с сортировкой, мы придём к размеру ввода (size) -> O(N)
// Общая: O(3*N) -> константу мы отбрасываем ВСЕГДА -> O(N)