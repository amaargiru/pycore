## **Администрирование/DevOps**

## gitflow!!!  
https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow

git

### Минимальный вариант <a name="gitflowminimum"></a>

git config --global core.editor "'C:/Program Files/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"  

Создать новый репозитарий  
в папке git init  
добавить файлы  
git add --all  
git commit  
Добавляем в текстовом файле первой строкой англоязычный заголовок коммита, второй и далее строками можно добавить русскоязычное описание. Сохраняем, закрываем.  
git branch --list список веток  
git branch small-update создает новую ветку, переключение на ветку не выполняется  
git checkout small-update переключается на вновь созданную ветку  
Делаем дополнения файлов в новой ветке  
git checkout master переключаемся на ветку master  
git merge small-update сливаем ветки  
git log --graph --full-history --all --color --pretty=format:"%x1b[31m%h%x09%x1b[32m%d%x1b[0m%x20%s"  

Слияние коммитов:  
git rebase  
squash 

Что такое Git Cherry pick?
Что такое форсированный push?
Что такое precommit check?
Что такое code cohesion & code coupling?

nginx

apache

Чем nginx отличается от apache

Источники!!!
