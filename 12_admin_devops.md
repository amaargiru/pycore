## 12. Администрирование/DevOps

> «О Уннефер, дай этому человеку в тоем Царстве тысячу хлебов, тысячу быков, тысячу сосудов пива».  
>  
> Обращение к Осирису, перевод М. Э. Матье.  

![DevOps](https://raw.githubusercontent.com/amaargiru/pycore/main/pics/12_DevOps.png)  

### Работа с git <a name="gitflowminimum"></a>

git config --global core.editor "'C:/Program Files/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"  

Создать новый репозитарий: git init  
Добавить файлы: git add --all  

git commit  
Добавляем в текстовом файле первой строкой англоязычный заголовок коммита, второй и далее строками можно добавить русскоязычное описание. Сохраняем, закрываем.  

Список веток: git branch --list  
Создаем новую ветку, переключение на ветку не выполняется: git branch small-update  
Переключение на вновь созданную ветку: git checkout small-update  
Переключение на ветку master: git checkout master  
Слияние веток: git merge small-update  
git log --graph --full-history --all --color --pretty=format:"%x1b[31m%h%x09%x1b[32m%d%x1b[0m%x20%s"  

Слияние коммитов:  
git rebase  
squash  

Попытка перенести одиночный коммит из ветки в ветку: cherry pick  
Правка истории git с риском затереть чужие коммиты: git push origin master --force-with-lease (форсированный push)  

## Precommit check

Хуки (скрипты на shell'ах или Python), позволяющие:
выполнять проверку отправляемого в репозиторий кода на валидность (PEP8, документация и т. д.);
выполнять комплексное тестирование проекта;
прерывать операцию commit'а в случае обнаружения ошибок и отображать подробный журнал ошибок.

### Базовые знания Linux и работа в консоли

Разумеется, администрирование подразумевает работу в консоли. Ничего сложного в этом нет, в конце концов, Анджелина Джоли в «Хакерах» и Кэрри-Энн Мосс в «Матрице» прекрасно справились!

CI/CD

Continuous testing
GitHub Actions
Jenkins

Containers

Docker
Kubernetes

### Git-flow

<img src="gitflow.svg" style="height:320px">

В целом, в настоящее время модель git-flow используется сравнительно редко. Эта модель ветвления основана на предсказуемом, долгосрочном цикле релиза новых версий, а не на выпуске нового кода каждые несколько часов. Git-flow сильно усложняет continuous delivery, когда разработчики выпускают частые обновления путем слияния с мастером (фактически, непосредственно в production) и плохо подходит для проектов, разбитых на сервисы.  
Единственный вариант, неплохо подходящий под git-flow — большая команда (20+ человек), планомерно выпускающая несколько параллельных релизов или занимающаяся поддержкой нескольких версий приложения параллельно. В таком случае git-flow действительно может помочь навести порядок.  

### Магистральная разработка

Магистральная разработка (trunk-based development) фактически является обязательной практикой CI/CD и предполагает небольшие частые обновления главной ветки. Подразумевает ежедневные коммиты, многоуровневое автоматическое тестирование и быструю кеширующую сборку.

## Источники  

### Python

Официальная документация Python [docs.python.org](https://docs.python.org/), включающая [The Python Standard Library](https://docs.python.org/3/library/index.html).  
Весьма подробное руководство (совсем уж базовый синтаксис не включен): [Comprehensive Python Cheatsheet](https://github.com/gto76/python-cheatsheet).  
Руководство с включением базового синтаксиса: [Python Cheatsheet](https://github.com/wilfredinni/python-cheatsheet). Включает практические Jupiter [Notebooks](https://github.com/wilfredinni/python-cheatsheet/tree/master/jupyter_notebooks).  
Сипсок библиотек и фреймворков: [Awesome Python](https://github.com/vinta/awesome-python).  
Около-питоновские практические советы (pip, virtualenv, pyInstaller и т. д.): ["The Hitchhiker’s Guide to Python"](https://github.com/realpython/python-guide).  
Мануал для начинающих дата-сайентистов: [Joel Grus, "Data Science from Scratch"](https://github.com/joelgrus/data-science-from-scratch).  
Руководство для начинающих: ["Python Notes for Professionals"](https://goalkicker.com/PythonBook/).  
Руководство для опытных программистов: ["Python 3 Patterns, Recipes and Idioms"](https://python-3-patterns-idioms-test.readthedocs.io/en/latest/index.html).  
Архитектурные паттерны: [Harry Percival & Bob Gregory, "Architecture Patterns with Python"](https://www.cosmicpython.com/book/preface.html).  

### Git

Статья 2010 года, положившая начало распростанения git-flow. Сам автор сделал в 2020 дополнение к статье, где рекомендует командам, придерживающихся continuous delivery, переходить на GitHub flow: [A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/).  
git-flow (компания Atlassian изменила текст страницы, теперь там размещены рекомендации перехода на магистральную разработку): [git-flow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow).  
[Критика](https://habr.com/ru/company/flant/blog/491320/) git-flow.  
[GitHub flow](https://docs.github.com/en/get-started/quickstart/github-flow).  
