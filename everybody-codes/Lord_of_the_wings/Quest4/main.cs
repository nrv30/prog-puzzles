public struct Participant 
{
    public Participant(int quest, int part, int time)
    {
        Quest = quest;
        Times = new int[3];
        Times[part] = time;
    }

    public int Quest;
    public int[] Times;
}


class Program
{
    static int ParseField(String s)
    {
        int eqIdx = s.IndexOf("=");
        return Int32.Parse(s.Substring(eqIdx + 1, s.Length - eqIdx - 1));    
    }

    static (int, int, int, int) ParseParticipant(String[] tokens)
    {
        int id    = ParseField(tokens[0]);
        int quest = ParseField(tokens[1]);
        int part  = ParseField(tokens[2]);
        int time  = ParseField(tokens[3]);

        return (id, quest, part, time);
    }

    static void printArray(int[] ints)
    {
        Console.Out.WriteLine($"{ints[0]}, {ints[1]}, {ints[2]}");
    }

    static int sumArray(int[] ints)
    {
        return ints[0] + ints[1] + ints[2];
    }

    static void Main()
    {
        Dictionary<int, Participant> results = new Dictionary<int, Participant>();

        var lines = File.ReadLines("input.txt");
        foreach (string line in lines)
        {
            var tokens = line.Split(' ');
            var (id, quest, part, time) = ParseParticipant(tokens);

            if (!results.ContainsKey(id))
            {
                Participant p = new Participant(quest, part - 1, time);
                results.Add(id, p);
            } else
            {
                results[id].Times[part - 1] = time;
            }
        }

        Dictionary<int, Participant>.KeyCollection keyColl = results.Keys;
        var sortedKeys = keyColl.OrderBy(key => sumArray(results[key].Times));

        Int64 checksum = 0;
        for(int i = 0; i < sortedKeys.Count(); i++) 
        {
            checksum += (i+1) * sumArray(results[sortedKeys.ElementAt(i)].Times);  
        }

        Console.Out.WriteLine(checksum);
    }
}