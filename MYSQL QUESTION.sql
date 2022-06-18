/*Fetch number of first message sent in a conversation in a day. Date range - 1st Jan 2021 to 31st
Dec 2021.*/

SELECT COUNT(DISTINCT(conversation_id)) FROM messages
INNER JOIN  conversations 
ON messages.conversation_id = conversations.id
GROUP BY created_at
HAVING 
created_at BETWEEN
'2021/01/01 00:00:00'
AND  
'2021/12/31 23:59:59'  
;


 /* Fetch number of first reply message sent in a conversation in a day. Date range - 1st Jan 2021 to
31st Dec 2021 */

SELECT COUNT(DISTINCT(conversation_id)) FROM messages INNER JOIN messages
ON conversations.id= messages.conversation_id
group by messages.conversation_id
HAVING sent_time BETWEEN  '2021/01/01 00:00:00'
AND   '2021/12/31 23:59:59'  
AND message.id > 
( SELECT MIN( message.id ) FROM  messages GROUP BY conversation_id )
ORDER BY message.id
LIMIT 1,2
;


/*Total conversation with 3 way messaging. 3 way messaging means User1 sent the message,
then User2 replied and finally User1 messaged back.
*/

SELECT COUNT(DISTINCT(conversation_id)) FROM conversations INNER JOIN messages
ON conversation.id= messages.conversation_id
group by messages.conversation_id
HAVING count(message.id)= 3
;