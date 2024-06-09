<?

ini_set('phar.readonly', 0);
class Requests
{
    public $url;
    private $options;
    private $postData;
    private $cookie;
    function __construct($url, $postData = '', $cookie = '', $options = array())
    {
        $this->url = $url;
        $this->postData = $postData;
        $this->cookie = $cookie;
        $this->options = $options;
    }

    function __destruct()
    {
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $this->url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

        if (!empty($this->postData)) {
            curl_setopt($ch, CURLOPT_POST, true);
            curl_setopt($ch, CURLOPT_POSTFIELDS, $this->postData);
        }

        if (!empty($this->cookie)) {
            curl_setopt($ch, CURLOPT_COOKIE, $this->cookie);
        }

        foreach ($this->options as $option => $value) {
            curl_setopt($ch, $option, $value);
        }

        $output = curl_exec($ch);
        echo $output;
        curl_close($ch);
    }
}