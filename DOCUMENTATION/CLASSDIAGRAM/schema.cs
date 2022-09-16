// Root myDeserializedClass = JsonConvert.DeserializeObject<List<Root>>(myJsonResponse);
    public class Analysis
    {
        public Analyzer analyzer { get; set; }
        public Tokenizer tokenizer { get; set; }
    }

    public class Analyzer
    {
        public NgramAnalyzer ngram_analyzer { get; set; }
    }

    public class NgramAnalyzer
    {
        public List<string> filter { get; set; }
        public string type { get; set; }
        public string tokenizer { get; set; }
    }

    public class NgramTokenizer
    {
        public List<string> token_chars { get; set; }
        public string min_gram { get; set; }
        public string type { get; set; }
        public string max_gram { get; set; }
    }

    public class Nodes
    {
        public string table { get; set; }
        public List<string> columns { get; set; }
        public Transform transform { get; set; }
    }

    public class Rename
    {
        public string website { get; set; }
        public string creation_date { get; set; }
        public string provider_domain { get; set; }
        public string author { get; set; }
        public string keywords { get; set; }
        public string date_created { get; set; }
        public string document { get; set; }
        public string paperabstract { get; set; }
        public string year { get; set; }
    }

    public class Root
    {
        public string database { get; set; }
        public string index { get; set; }
        public Setting setting { get; set; }
        public Nodes nodes { get; set; }
    }

    public class Setting
    {
        public Analysis analysis { get; set; }
    }

    public class Tokenizer
    {
        public NgramTokenizer ngram_tokenizer { get; set; }
    }

    public class Transform
    {
        public Rename rename { get; set; }
    }

