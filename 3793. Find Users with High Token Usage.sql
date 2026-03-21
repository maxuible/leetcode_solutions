/* Write your T-SQL query statement below */
SELECT
p.user_id,
COUNT(p.Tokens) as prompt_count,
ROUND(SUM( CAST(p.Tokens as float))/COUNT(CAST(p.Tokens as float)),2) as avg_tokens
  FROM prompts as p
group by p.user_id
having count(p.tokens) >= 3
and MAX(p.tokens) > ROUND(SUM( CAST(p.Tokens as float))/COUNT(CAST(p.Tokens as float)),2)
order by ROUND(SUM( CAST(p.Tokens as float))/COUNT(CAST(p.Tokens as float)),2) desc, user_id