use foofle_proj;

CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(50) NOT NULL PRIMARY KEY,
    pass VARCHAR(50) NOT NULL,
    signupdate TIMESTAMP,
    accountphone VARCHAR(15),
    permitall int default 1
);
 

CREATE TABLE info (
    address VARCHAR(128) default null,
    firstname VARCHAR(30)default null,
    lastname VARCHAR(30)default null,
    nickname VARCHAR(30)default null,
    phone VARCHAR(30)default null,
    birthdate DATE default null,
    nationalityID varchar(30)default null,
    nid VARCHAR(30),
    FOREIGN KEY (nid) REFERENCES users (username) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Logins (
    id INT AUTO_INCREMENT,
    username VARCHAR(30),
    time_in TIMESTAMP,
    FOREIGN KEY (username)
        REFERENCES users (username)
        ON UPDATE CASCADE ON DELETE CASCADE,
    PRIMARY KEY (id)
);
                    
CREATE TABLE news (
    id INT AUTO_INCREMENT,
    newsTime TIMESTAMP,
    title VARCHAR(256),
    body VARCHAR(512),
    username VARCHAR(30),
    PRIMARY KEY (id),
    FOREIGN KEY (username)
        REFERENCES users (username)
        ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE email (
    id INT AUTO_INCREMENT,
    usern VARCHAR(50),
    mail_subject VARCHAR(30),
    timesent TIMESTAMP,
    body VARCHAR(512),
    mail_status VARCHAR(30),
    PRIMARY KEY (id),
    FOREIGN KEY (usern)
        REFERENCES users (username)
        ON UPDATE CASCADE ON DELETE CASCADE
);
                    
 
CREATE TABLE recivers (
    id INT,
    username VARCHAR(30),
    mail_status INT,
    FOREIGN KEY (username)
        REFERENCES users (username)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (id)
        REFERENCES email (id)
);


create table permissionEXP(username varchar(30),
							blockeduser varchar(30),
                            foreign key(username) references users(username));

delimiter $$
create procedure changepermissionstate(in Username varchar(30))
begin
declare outp int;
call getpermitstatus(Username,outp);
select outp;
if outp=1 then
	update users set permitall=0 where users.username=Username;
    else update users set permitall=1 where users.username=Username;
    end if;
    delete from permissionEXP where permissionEXP.username=Username;
    -- UPDATE permissionEXP SET blockeduser = NULL WHERE blockeduser is not null and permissionEXP.username=Username;
end $$
delimiter ;


delimiter $$
create procedure getpermitstatus(in Username varchar(30), out valueamount int)
begin
select permitAll into valueamount from users where users.username=Username;
end $$
delimiter ; 


delimiter $$ 
create procedure blockinfo(in Username varchar(30), in blockuser varchar(30))
begin
	if blockuser in (select blockeduser from permissionEXP where permissionEXP.username=username) then
		delete from permissionEXP where permissionEXP.username=Username;
	else 
		if Username in (select username from permissionEXP where blockeduser=null) then
			delete from permissionEXP where permissionEXP.username=Username;
		end if;
		insert into permissionEXP(username,blockeduser) values(Username,blockuser);
	end if;
end $$
delimiter ;


delimiter $$
create procedure permission(in Username varchar(30), in checkuser varchar(30))
begin
	declare outp int;
	call getpermitstatus(Username,outp);
	if outp=1 then
		if checkuser not in(select blockeduser from permissionEXP where permissionEXP.username=Username) then 
			select firstname,lastname,nickname,phone,nationalityID,birthdate,address from info where info.nid=Username;
		else select "***" as firstname,"***" as lastname,"***" as nickname
            ,"***" as phone,"***" as nationalityID,"***" as birthdate,"***" as address;
            end if;
		else 
			if checkuser in(select blockeduser from permissionEXP where permissionEXP.username=Username) then
				select firstname,lastname,nickname,phone,nationalityID,birthdate,address from info where info.nid=Username;
			else select "***" as firstname,"***" as lastname,"***" as nickname
            ,"***" as phone,"***" as nationalityID,"***" as birthdate,"***" as address;
			end if;
	end if;
end $$
delimiter ;

delimiter $$
create procedure permissionnews(in Username varchar(30),in checkuser varchar(30))
begin
	insert into news(newsTime,title,body,username) values (current_timestamp(),'ask for permission',concat(checkuser,'wants to see your info.
    if you want to change your privacy state for them,click the button below.'),Username);
end $$
delimiter ;


delimiter $$
create procedure Fetchnews(in inUsername varchar(30))
begin
	select title,body from news
    where news.username = inusername
    order by id desc;
end $$
Delimiter ;

delimiter $$
create procedure deletereciver(in username varchar(30), in mail_id int)
begin
  update recivers set mail_status='deleted'
    where recivers.username=Username and recivers.id=mail_id;
end $$
delimiter ;


delimiter &&
create procedure userscheckpass(in Username varchar(30), in passw varchar(30)) -- ,out un varchar(30))
begin
	declare newpass varchar(50);
    set newpass=md5(passw);
    if Username not in(select username from users where users.username=Username) then
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'user not found!';
    end if;
    if newpass not in(select pass from users where users.username=Username) then
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'wrong password!';
	end if;
    select username  
    from users 
    where users.username=Username and pass=newpass;
end &&
delimiter ;

delimiter $$
create procedure checkcasecade(in Username varchar(30))
BEGIN
	select username from users where LOWER(users.username)=lower(Username);
end $$
delimiter ;

delimiter $$
create procedure AddToLoginTable(in username varchar(30)) 
begin 
	insert into Logins(username,time_in) values(username,current_timestamp());
end $$
Delimiter ;

					                 
Delimiter $$
create procedure addInfo(in address varchar(128),
						 in firstname varchar(30),
						 in lastname varchar(30),
						 in nickname varchar(30),
						 in phone varchar(30),
                         in nationalityID varchar(30),
						 in birthdate date,
						 in nid varchar(30),
                         in accountphone varchar(30),
                         in pass varchar(30)) 
begin 
	if length(pass)< 6 then
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'password length should be at least 6 characters';
    end if;
	update users set accountphone=accountphone,pass=pass where username=nid;
	update info set address=address,firstname=firstname,lastname=lastname,nickname=nickname,phone=phone,nationalityID=nationalityID,birthdate=birthdate where info.nid=nid;
end $$
delimiter ;


delimiter $$
create procedure getInfo(in Username varchar(30))
begin
	select * 
    from users,info
    where users.username = Username and info.nid=users.username;
end $$
delimiter ;

select * from info
call getInfo('gorbeh')

delimiter $$
create procedure otherUsersInfo(in Username varchar(30))
begin 
	IF EXISTS (SELECT * FROM users WHERE username = Username) then
		select * from info 
		where info.nid=Username;
	end if;
end $$
delimiter ; 

delimiter $$
create procedure DeleteUser(in Username varchar(30))
begin 
	delete from users 
    where users.username=Username;
end $$
delimiter ;


delimiter $$
create procedure addNewUser(in Username varchar(50),in pass varchar(50),in phone varchar(12),in fn varchar(30),in ln varchar(30),in nn varchar(30),in ntid varchar(30),in bd DATE,in ph2 varchar(30),in addrs varchar(128))
begin
DECLARE CONTINUE HANDLER FOR 1062
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'this username already exists';
  if length(Username)> 5 then
	if length(pass)> 5 then
			insert into users(username,pass,signupdate,accountphone) values(Username,MD5(pass),current_timestamp(),phone);
            update info set firstname=fn,lastname=ln,nickname=nn,nationalityID=ntid,birthdate=bd,phone=ph2,address=addrs;
    else SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'password length should be at least 6 characters';
	end if;
  else SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'username length has to be more than 5 characters';
  end if;
end $$
 delimiter ;

 
 delimiter $$
create procedure getlastlogin()
begin
  select username from Logins order by id desc limit 1;
end $$
delimiter ;


delimiter $$
create procedure addnewmail(in msubject varchar(30), in body varchar(512), in username varchar(50))
BEGIN
if SUBSTRING_INDEX(username, '@', 1) not in (select username from users where users.username=username) then
SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'invalid user';
end if;
insert into email (usern,mail_subject,timesent,body,mail_status) values(username,msubject,current_timestamp,body,'sent');
end $$
delimiter ;


delimiter $$
create procedure addtorecivers(in username varchar(30))
begin
	declare theusername varchar(30);
	DECLARE lastemailid INT;
	set lastemailid =(select max(id) from email);
    set theusername=SUBSTRING_INDEX(username,'@', 1);
	insert into recivers values(lastemailid,username,1);
end $$
delimiter ;


delimiter $$
create procedure deletemailforuser(in username varchar(30), in mail_id int)
begin
  update recivers set mail_status='-1'
    where recivers.username=Username and recivers.id=mail_id;
end $$
delimiter ;

delimiter $$
create procedure getinbox(in Username varchar(30))
begin 
	select email.id,mail_subject,body,recivers.mail_status
    from email ,recivers
    where recivers.id=email.id and recivers.username=Username and recivers.mail_status!='-1'
    order by email.timesent desc;
end $$
delimiter ;


delimiter $$
create procedure getsent(in Username varchar(30))
begin
  select mail_subject,body,mail_status,email.id
    from email
    where email.usern=Username and email.mail_status!= '0'
    order by email.timesent desc;
end $$
delimiter ;



delimiter $$
create procedure readmail(in username varchar(30), in mail_id int)
begin
	update recivers set mail_status=0
    where recivers.username=Username and recivers.id=mail_id;
end $$
delimiter ;


delimiter $$
create procedure deletemail(in mail_id int)
begin
	update email set mail_status='0'
    where email.id=mail_id;
end $$
delimiter ;

delimiter $$
create procedure deletenews(in id int)
begin
	delete from news where news.id=id;
end $$
delimiter ;


CREATE 
    TRIGGER  Login
 before INSERT ON Logins FOR EACH ROW 
    INSERT INTO news (newsTime , title , body , username) VALUES (CURRENT_TIMESTAMP() , 'news on login' , CONCAT('logged in at', CURRENT_TIMESTAMP()) , new.username);


CREATE 
    TRIGGER  mailsent
 AFTER INSERT ON recivers FOR EACH ROW 
    INSERT INTO news(newsTime,title,body,username) VALUES (CURRENT_TIMESTAMP() , 'you have new mail' , 'new mail arrived' , new.username);



CREATE 
    TRIGGER  maildeleted
 AFTER UPDATE ON email FOR EACH ROW 
    INSERT INTO news(newsTime,title,body,username) VALUES (CURRENT_TIMESTAMP , 'mail deleted' , 'mail is deleted' , new.usern);


CREATE 
    TRIGGER  useraddnews
 AFTER INSERT ON users FOR EACH ROW 
    INSERT INTO news(newsTime,title,body,username) VALUES (CURRENT_TIMESTAMP , 'Welcome' , 'WELCOME TO FOOFLE!' , NEW.username);


CREATE 
    TRIGGER  EditInfoNews
 AFTER UPDATE ON info FOR EACH ROW 
    INSERT INTO news(newsTime,title,body,username) VALUES (CURRENT_TIMESTAMP , 'news on edit' , 'info successfully edited.',new.nid);

CREATE 
    TRIGGER  addInfoRow
 AFTER INSERT ON users FOR EACH ROW 
    INSERT INTO info (nid) VALUES (new.username);
    
CREATE TRIGGER sentmailnews
after insert on email for each row
	insert into news(newsTime,title,body,username) VALUES (CURRENT_TIMESTAMP , 'news on sent', 'mail sent', new.usern);
