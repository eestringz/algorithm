SELECT 
    I.ITEM_ID,
    I.ITEM_NAME,
    I.RARITY
FROM 
    ITEM_INFO AS I
LEFT JOIN
  ITEM_TREE AS T ON T.PARENT_ITEM_ID = I.ITEM_ID
WHERE 
    ISNULL(T.PARENT_ITEM_ID)
ORDER BY 
    I.ITEM_ID DESC;