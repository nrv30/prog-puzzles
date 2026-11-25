param (
    [Parameter(Mandatory=$true)]
    [string] $filepath
)

function RevIdx {
    param(
        [int] $i, 
        [int] $Length
    )
    return $Length - ($i + 1)
}

function RevString {
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
        $targetIndex = RevIdx $i $string.Length
        [void] $sb.Append($string[$targetIndex])
    }
    return $sb.ToString()
}

[int64] $checksum = 0
Get-Content $filepath | Foreach-Object {
    $ISOStand, $vote = $_ -split ' '

    $delimIdx = $ISOStand.IndexOf('-')
    $standVersion = $_.Substring($delimIdx + 1, $ISOStand.Length - $delimIdx).Trim()
    
    [int64] $sum = 0
    if ($vote.Length -ne $standVersion.Length)
    {
        $sb = [System.Text.StringBuilder]::new()
        $revStand = RevString $sb $standVersion $([Math]::Min($vote.Length, $standVersion.Length))
        [void] $sb.clear()
        [void] $sb.Append($revStand)
        $diff = $vote.Length - $standVersion.Length
        for ($i = 0; $i -lt $diff; $i++) 
        {
            $idx = $i % $standVersion.Length
            $idx = RevIdx $idx $standVersion.Length 

            [void] $sb.Append($standVersion[$idx])
        }
        $standVersion = $sb.ToString()
        [void] $sb.Clear()
        $standVersion = RevString $sb $standVersion
        # echo "ISO Standard $standVersion"
    } 
    
    for ($i = 0; $i -lt $vote.Length; $i++) 
    {
        # $place = $vote.Length - ($i + 1)
        $place = RevIdx $i $vote.Length
        $sum += [Math]::Pow([int]::Parse($standVersion[$i]), $place) * [int]::Parse($vote[$i])
    }

    # echo $sum
    $checksum += $sum
    # exit(1)
}

Write-Output $checksum