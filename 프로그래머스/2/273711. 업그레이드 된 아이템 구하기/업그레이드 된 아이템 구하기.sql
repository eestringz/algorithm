-- 코드를 작성해주세요
SELECT a.ITEM_ID, a.ITEM_NAME, a.RARITY
FROM ITEM_INFO AS a
INNER JOIN ITEM_TREE as b ON a.ITEM_ID = b.ITEM_ID
WHERE b.PARENT_ITEM_ID IN (
    SELECT ITEM_ID
    FROM ITEM_INFO
    WHERE RARITY = 'RARE'
)
ORDER BY a.ITEM_ID DESC

