param (
    [Parameter(Mandatory=$true)]
    [string] $filepath
)

$sw = [System.Diagnostics.Stopwatch]::StartNew()
[int64] $checksum = (
    Get-Content $filepath | Foreach-Object -Parallel {

    function revIdx 
    {
        param(
            [int] $i, 
            [int] $Length
        )
        return $Length - ($i + 1)
    }

    function revString 
    {
        param(
            [System.Text.StringBuilder] $sb,
            [string] $string,
            [int] $n = 0
        )

        if ($n -eq 0)
        {
            $n = $string.Length
        }

        for ($i = 0; $i -lt $n; $i++)
        {
            $targetIndex = revIdx $i $string.Length
            [void] $sb.Append($string[$targetIndex])
        }
        return $sb.ToString()
    }

    function toDecimal 
    {
        param (
            [string] $standVersion,
            [string] $vote
        )

        [int64] $sum = 0
        for ($i = 0; $i -lt $vote.Length; $i++) 
        {
            $place = revIdx $i $vote.Length
            $sum += [Math]::Pow([int]::Parse($standVersion[$i]), $place) * [int]::Parse($vote[$i])
        }

        return $sum
    }

    function ensureDigitsMatch 
    {
        param (
            [string] $standVersion
        )

        $sb = [System.Text.StringBuilder]::new()
        $revStand = revString $sb $standVersion $([Math]::Min($vote.Length, $standVersion.Length))
        [void] $sb.clear()
        [void] $sb.Append($revStand)
        $diff = $vote.Length - $standVersion.Length
        for ($i = 0; $i -lt $diff; $i++) 
        {
            $idx = $i % $standVersion.Length
            $idx = revIdx $idx $standVersion.Length 

            [void] $sb.Append($standVersion[$idx])
        }
        $standVersion = $sb.ToString()
        [void] $sb.Clear()
        return revString $sb $standVersion
    }

    function convertVote 
    {
        param (
            [string] $standVersion,
            [string] $vote
        )

        if ($vote.Length -ne $standVersion.Length)
        {
            [string] $standVersion = ensureDigitsMatch $standVersion
        }

        return toDecimal $standVersion $vote
    }

    function isValidIso2 
    {
        param (
            [string] $standVersion,
            [int64] $vote,
            [int64] $voteAsDecimal
        )

        for ($i = 1; $i -lt $vote; $i++)
        {
            $other = convertVote $standVersion $i
            if ($other -eq $voteAsDecimal)
            {
                return $false
            }
        }

        return $true
    }

    function doThing 
    {
        param (
            [string] $line
        )

        $ISOStand, $vote = $_ -split ' '

        $delimIdx = $ISOStand.IndexOf('-')
        $standVersion = $_.Substring($delimIdx + 1, $ISOStand.Length - $delimIdx).Trim()
        
        $voteAsDecimal = convertVote $standVersion $vote

        $voteAsInt = [int]::Parse($vote)
        if (-not (isValidIso2 $standVersion $voteAsInt $voteAsDecimal))
        {
            write-host "invalid"
            return 0
        }
        
        write-host "$voteAsDecimal"
        return $voteAsDecimal
}
        doThing -line $_
    }
) | Measure-Object -Sum | Select-Object -ExpandProperty Sum

write-host $checksum
$sw.stop()
$sw.Elapsed