


<!DOCTYPE html>
<html lang="en" class="">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    
    
    <title>COMP1-2015/Comp1_Summer_2015_Python3Pub0.0.0.py at master · longroadcomputing/COMP1-2015</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="longroadcomputing/COMP1-2015" name="twitter:title" /><meta content="COMP1-2015 - Preliminary materials and tasks for 2015 COMP1 exam" name="twitter:description" /><meta content="https://avatars0.githubusercontent.com/u/5710156?v=3&amp;s=400" name="twitter:image:src" />
      <meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars0.githubusercontent.com/u/5710156?v=3&amp;s=400" property="og:image" /><meta content="longroadcomputing/COMP1-2015" property="og:title" /><meta content="https://github.com/longroadcomputing/COMP1-2015" property="og:url" /><meta content="COMP1-2015 - Preliminary materials and tasks for 2015 COMP1 exam" property="og:description" />
      <meta name="browser-stats-url" content="/_stats">
    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="xhr-socket" href="/_sockets">
    <meta name="pjax-timeout" content="1000">
    <link rel="sudo-modal" href="/sessions/sudo_modal">

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="D4DB6D01:6171:60466:55157F47" name="octolytics-dimension-request_id" /><meta content="8697125" name="octolytics-actor-id" /><meta content="RyanLongRoad" name="octolytics-actor-login" /><meta content="8687b1f04b5230c60884b24eaef82c1222493aa9702bbfe01609900153bf8190" name="octolytics-actor-hash" />
    
    <meta content="Rails, view, blob#show" name="analytics-event" />

    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">


    <meta content="authenticity_token" name="csrf-param" />
<meta content="7/gyO46WSmlBxR10L1zD+73wxyREXCCWd77evZr5fCrFzah3a2h5vIwAOqIMdvhZ58V29j4JsmY7Oge2GFwzwQ==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github-72aef5c1eab64bf684cb6f55513fae147b11b63503bf2311319ec22e77d3194f.css" media="all" rel="stylesheet" />
    <link href="https://assets-cdn.github.com/assets/github2-40d9bf14363443ccf64a2b71208f59e8739d6288d962feba121227e0608772f3.css" media="all" rel="stylesheet" />
    
    


    <meta http-equiv="x-pjax-version" content="16f1961eb9229a014751d96dc0a55124">

      
  <meta name="description" content="COMP1-2015 - Preliminary materials and tasks for 2015 COMP1 exam">
  <meta name="go-import" content="github.com/longroadcomputing/COMP1-2015 git https://github.com/longroadcomputing/COMP1-2015.git">

  <meta content="5710156" name="octolytics-dimension-user_id" /><meta content="longroadcomputing" name="octolytics-dimension-user_login" /><meta content="32520381" name="octolytics-dimension-repository_id" /><meta content="longroadcomputing/COMP1-2015" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="32520381" name="octolytics-dimension-repository_network_root_id" /><meta content="longroadcomputing/COMP1-2015" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/longroadcomputing/COMP1-2015/commits/master.atom" rel="alternate" title="Recent Commits to COMP1-2015:master" type="application/atom+xml">

  </head>


  <body class="logged_in  env-production windows vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      


        <div class="header header-logged-in true" role="banner">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <span class="mega-octicon octicon-mark-github"></span>
</a>


      <div class="site-search repo-scope js-site-search" role="search">
          <form accept-charset="UTF-8" action="/longroadcomputing/COMP1-2015/search" class="js-site-search-form" data-global-search-url="/search" data-repo-search-url="/longroadcomputing/COMP1-2015/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
  <input type="text"
    class="js-site-search-field is-clearable"
    data-hotkey="s"
    name="q"
    placeholder="Search"
    data-global-scope-placeholder="Search GitHub"
    data-repo-scope-placeholder="Search"
    tabindex="1"
    autocapitalize="off">
  <div class="scope-badge">This repository</div>
</form>
      </div>
      <ul class="header-nav left" role="navigation">
        <li class="header-nav-item explore">
          <a class="header-nav-link" href="/explore" data-ga-click="Header, go to explore, text:explore">Explore</a>
        </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://gist.github.com" data-ga-click="Header, go to gist, text:gist">Gist</a>
          </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="/blog" data-ga-click="Header, go to blog, text:blog">Blog</a>
          </li>
        <li class="header-nav-item">
          <a class="header-nav-link" href="https://help.github.com" data-ga-click="Header, go to help, text:help">Help</a>
        </li>
      </ul>

    
<ul class="header-nav user-nav right" id="user-links">
  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link name" href="/RyanLongRoad" data-ga-click="Header, go to profile, text:username">
      <img alt="@RyanLongRoad" class="avatar" data-user="8697125" height="20" src="https://avatars0.githubusercontent.com/u/8697125?v=3&amp;s=40" width="20" />
      <span class="css-truncate">
        <span class="css-truncate-target">RyanLongRoad</span>
      </span>
    </a>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link js-menu-target tooltipped tooltipped-s" href="#" aria-label="Create new..." data-ga-click="Header, create new, icon:add">
      <span class="octicon octicon-plus"></span>
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      
<ul class="dropdown-menu">
  <li>
    <a href="/new" data-ga-click="Header, create new repository, icon:repo"><span class="octicon octicon-repo"></span> New repository</a>
  </li>
  <li>
    <a href="/organizations/new" data-ga-click="Header, create new organization, icon:organization"><span class="octicon octicon-organization"></span> New organization</a>
  </li>


    <li class="dropdown-divider"></li>
    <li class="dropdown-header">
      <span title="longroadcomputing/COMP1-2015">This repository</span>
    </li>
      <li>
        <a href="/longroadcomputing/COMP1-2015/issues/new" data-ga-click="Header, create new issue, icon:issue"><span class="octicon octicon-issue-opened"></span> New issue</a>
      </li>
</ul>

    </div>
  </li>

  <li class="header-nav-item">
        <a href="/notifications" aria-label="You have no unread notifications" class="header-nav-link notification-indicator tooltipped tooltipped-s" data-ga-click="Header, go to notifications, icon:read" data-hotkey="g n">
        <span class="mail-status all-read"></span>
        <span class="octicon octicon-inbox"></span>
</a>
  </li>

  <li class="header-nav-item">
    <a class="header-nav-link tooltipped tooltipped-s" href="/settings/profile" id="account_settings" aria-label="Settings" data-ga-click="Header, go to settings, icon:settings">
      <span class="octicon octicon-gear"></span>
    </a>
  </li>

  <li class="header-nav-item">
    <form accept-charset="UTF-8" action="/logout" class="logout-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="e8ci82Vgr0Z4bGu0TIg3Iq6xTzakViBxoEsgankphCM+HveJD+Hg/GGHojm1fOv/hvqPBqazQuMBCm8wnhGYtQ==" /></div>
      <button class="header-nav-link sign-out-button tooltipped tooltipped-s" aria-label="Sign out" data-ga-click="Header, sign out, icon:logout">
        <span class="octicon octicon-sign-out"></span>
      </button>
</form>  </li>

</ul>


    
  </div>
</div>

        

        
<div class="flash-global js-notice flash-warn">
<div class="container">
    <h2>
      You don't have any verified emails.  We recommend <a href="https://github.com/settings/emails">verifying</a> at least one email.
    </h2>
    <p>
Email verification helps our support team verify ownership if you lose account access and allows you to receive all the notifications you ask for.
    </p>


















</div>
</div>


      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        
<ul class="pagehead-actions">

  <li>
      <form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="ToGTpy+pK7JO1253n7OkXCBi+wpJZsGU5uKBcEFlBW5U7sWAFdIDPvMBXCBI+CunYiWaKuTdyZb6ykBZs9SBbw==" /></div>    <input id="repository_id" name="repository_id" type="hidden" value="32520381" />

      <div class="select-menu js-menu-container js-select-menu">
        <a href="/longroadcomputing/COMP1-2015/subscription"
          class="btn btn-sm btn-with-count select-menu-button js-menu-target" role="button" tabindex="0" aria-haspopup="true"
          data-ga-click="Repository, click Watch settings, action:blob#show">
          <span class="js-select-button">
            <span class="octicon octicon-eye"></span>
            Watch
          </span>
        </a>
        <a class="social-count js-social-count" href="/longroadcomputing/COMP1-2015/watchers">
          2
        </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
            <div class="select-menu-header">
              <span class="select-menu-title">Notifications</span>
              <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
            </div>

            <div class="select-menu-list js-navigation-container" role="menu">

              <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input checked="checked" id="do_included" name="do" type="radio" value="included" />
                  <span class="select-menu-item-heading">Not watching</span>
                  <span class="description">Be notified when participating or @mentioned.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-eye"></span>
                    Watch
                  </span>
                </div>
              </div>

              <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input id="do_subscribed" name="do" type="radio" value="subscribed" />
                  <span class="select-menu-item-heading">Watching</span>
                  <span class="description">Be notified of all conversations.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-eye"></span>
                    Unwatch
                  </span>
                </div>
              </div>

              <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input id="do_ignore" name="do" type="radio" value="ignore" />
                  <span class="select-menu-item-heading">Ignoring</span>
                  <span class="description">Never be notified.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-mute"></span>
                    Stop ignoring
                  </span>
                </div>
              </div>

            </div>

          </div>
        </div>
      </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">

    <form accept-charset="UTF-8" action="/longroadcomputing/COMP1-2015/unstar" class="js-toggler-form starred js-unstar-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="sDJsWvakr6dCDj86KoMSpMLQlG3SZbizx2V681yqptPLO+mZc0IEiqaMmCBJ78aswPylDgZLVUNuhkLtiWYEXA==" /></div>
      <button
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar longroadcomputing/COMP1-2015"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <span class="octicon octicon-star"></span>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/longroadcomputing/COMP1-2015/stargazers">
          0
        </a>
</form>
    <form accept-charset="UTF-8" action="/longroadcomputing/COMP1-2015/star" class="js-toggler-form unstarred js-star-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="JyLCMrgDKekx8Ohpn2vE/SOmCxGxu9usRtJDQKcfOpaZ4offmVEYENqmcEJNuj3KqGXNRF0VvM0u7MwmyeCbUQ==" /></div>
      <button
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star longroadcomputing/COMP1-2015"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <span class="octicon octicon-star"></span>
        Star
      </button>
        <a class="social-count js-social-count" href="/longroadcomputing/COMP1-2015/stargazers">
          0
        </a>
</form>  </div>

  </li>

        <li>
          <form accept-charset="UTF-8" action="/longroadcomputing/COMP1-2015/fork" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="mV+lrZ6t1EjtD/1CIwL7L8cOiDjP4g3mQvNGiM+szEPFhlbW2akKhrN+IsU3poU5Rgt9kew4gM1U4I49XYEmnw==" /></div>
            <button
                type="submit"
                class="btn btn-sm btn-with-count"
                data-ga-click="Repository, show fork modal, action:blob#show; text:Fork"
                title="Fork your own copy of longroadcomputing/COMP1-2015 to your account"
                aria-label="Fork your own copy of longroadcomputing/COMP1-2015 to your account">
              <span class="octicon octicon-repo-forked"></span>
              Fork
            </button>
            <a href="/longroadcomputing/COMP1-2015/network" class="social-count">4</a>
</form>        </li>

</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="mega-octicon octicon-repo"></span>
          <span class="author"><a href="/longroadcomputing" class="url fn" itemprop="url" rel="author"><span itemprop="title">longroadcomputing</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/longroadcomputing/COMP1-2015" class="js-current-repository" data-pjax="#js-repo-pjax-container">COMP1-2015</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            
<nav class="sunken-menu repo-nav js-repo-nav js-sidenav-container-pjax js-octicon-loaders"
     role="navigation"
     data-pjax="#js-repo-pjax-container"
     data-issue-count-url="/longroadcomputing/COMP1-2015/issues/counts">
  <ul class="sunken-menu-group">
    <li class="tooltipped tooltipped-w" aria-label="Code">
      <a href="/longroadcomputing/COMP1-2015" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /longroadcomputing/COMP1-2015">
        <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Issues">
        <a href="/longroadcomputing/COMP1-2015/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /longroadcomputing/COMP1-2015/issues">
          <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
          <span class="js-issue-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>      </li>

    <li class="tooltipped tooltipped-w" aria-label="Pull requests">
      <a href="/longroadcomputing/COMP1-2015/pulls" aria-label="Pull requests" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g p" data-selected-links="repo_pulls /longroadcomputing/COMP1-2015/pulls">
          <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull requests</span>
          <span class="js-pull-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Wiki">
        <a href="/longroadcomputing/COMP1-2015/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g w" data-selected-links="repo_wiki /longroadcomputing/COMP1-2015/wiki">
          <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>      </li>
  </ul>
  <div class="sunken-menu-separator"></div>
  <ul class="sunken-menu-group">

    <li class="tooltipped tooltipped-w" aria-label="Pulse">
      <a href="/longroadcomputing/COMP1-2015/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-selected-links="pulse /longroadcomputing/COMP1-2015/pulse">
        <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

    <li class="tooltipped tooltipped-w" aria-label="Graphs">
      <a href="/longroadcomputing/COMP1-2015/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_graphs repo_contributors /longroadcomputing/COMP1-2015/graphs">
        <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>
  </ul>


</nav>

              <div class="only-with-full-nav">
                  
<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><span class="text-emphasized">HTTPS</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/longroadcomputing/COMP1-2015.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="ssh"
  data-url="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=clone">
  <h3><span class="text-emphasized">SSH</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="git@github.com:longroadcomputing/COMP1-2015.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><span class="text-emphasized">Subversion</span> checkout URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/longroadcomputing/COMP1-2015" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>



<p class="clone-options">You can clone with
  <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>, <a href="#" class="js-clone-selector" data-protocol="ssh">SSH</a>, or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</p>


  <a href="github-windows://openRepo/https://github.com/longroadcomputing/COMP1-2015" class="btn btn-sm sidebar-button" title="Save longroadcomputing/COMP1-2015 to your computer and use it in GitHub Desktop." aria-label="Save longroadcomputing/COMP1-2015 to your computer and use it in GitHub Desktop.">
    <span class="octicon octicon-device-desktop"></span>
    Clone in Desktop
  </a>

                <a href="/longroadcomputing/COMP1-2015/archive/master.zip"
                   class="btn btn-sm sidebar-button"
                   aria-label="Download the contents of longroadcomputing/COMP1-2015 as a zip file"
                   title="Download the contents of longroadcomputing/COMP1-2015 as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          

<a href="/longroadcomputing/COMP1-2015/blob/c86277a516bc14fe8fba941df91508700b64c084/Comp1_Summer_2015_Python3Pub0.0.0.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:963199fb6513e552011cda59c6e2ce00 -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu js-menu-container js-select-menu left">
  <span class="btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    title="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/longroadcomputing/COMP1-2015/blob/master/Comp1_Summer_2015_Python3Pub0.0.0.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="master">
                master
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

  <div class="btn-group right">
    <a href="/longroadcomputing/COMP1-2015/find/master"
          class="js-show-file-finder btn btn-sm empty-icon tooltipped tooltipped-s"
          data-pjax
          data-hotkey="t"
          aria-label="Quickly jump between files">
      <span class="octicon octicon-list-unordered"></span>
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
  </div>

  <div class="breadcrumb js-zeroclipboard-target">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/longroadcomputing/COMP1-2015" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">COMP1-2015</span></a></span></span><span class="separator">/</span><strong class="final-path">Comp1_Summer_2015_Python3Pub0.0.0.py</strong>
  </div>
</div>


  <div class="commit file-history-tease">
    <div class="file-history-tease-header">
        <img alt="@MrAGi" class="avatar" data-user="1733339" height="24" src="https://avatars0.githubusercontent.com/u/1733339?v=3&amp;s=48" width="24" />
        <span class="author"><a href="/MrAGi" rel="contributor">MrAGi</a></span>
        <time datetime="2015-03-19T12:38:14Z" is="relative-time">Mar 19, 2015</time>
        <div class="commit-title">
            <a href="/longroadcomputing/COMP1-2015/commit/01a8e569da3476b86d910bd1b71b00f7b9c685df" class="message" data-pjax="true" title="initial commit

Signed-off-by: Adam McNicol &lt;adam@mcnicol.me&gt;">initial commit</a>
        </div>
    </div>

    <div class="participation">
      <p class="quickstat">
        <a href="#blob_contributors_box" rel="facebox">
          <strong>1</strong>
           contributor
        </a>
      </p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img alt="@MrAGi" data-user="1733339" height="24" src="https://avatars0.githubusercontent.com/u/1733339?v=3&amp;s=48" width="24" />
            <a href="/MrAGi">MrAGi</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file">
  <div class="file-header">
    <div class="file-actions">

      <div class="btn-group">
        <a href="/longroadcomputing/COMP1-2015/raw/master/Comp1_Summer_2015_Python3Pub0.0.0.py" class="btn btn-sm " id="raw-url">Raw</a>
          <a href="/longroadcomputing/COMP1-2015/blame/master/Comp1_Summer_2015_Python3Pub0.0.0.py" class="btn btn-sm js-update-url-with-hash">Blame</a>
        <a href="/longroadcomputing/COMP1-2015/commits/master/Comp1_Summer_2015_Python3Pub0.0.0.py" class="btn btn-sm " rel="nofollow">History</a>
      </div>

        <a class="octicon-btn tooltipped tooltipped-nw"
           href="github-windows://openRepo/https://github.com/longroadcomputing/COMP1-2015?branch=master&amp;filepath=Comp1_Summer_2015_Python3Pub0.0.0.py"
           aria-label="Open this file in GitHub for Windows">
            <span class="octicon octicon-device-desktop"></span>
        </a>

            <form accept-charset="UTF-8" action="/longroadcomputing/COMP1-2015/edit/master/Comp1_Summer_2015_Python3Pub0.0.0.py" class="inline-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="khv00klkBmb8T4XpWUbZyLkbcW0AQgRWgJWXSZvUaYPTpkvReMDShfCRmf9azB7f5N4l7LH21B8lUMztOqzzNQ==" /></div>
              <button class="octicon-btn tooltipped tooltipped-n" type="submit" aria-label="Clicking this button will fork this project so you can edit the file" data-hotkey="e" data-disable-with>
                <span class="octicon octicon-pencil"></span>
              </button>
</form>
          <form accept-charset="UTF-8" action="/longroadcomputing/COMP1-2015/delete/master/Comp1_Summer_2015_Python3Pub0.0.0.py" class="inline-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="yOt+G2iTUrpGHaDSodqggjWe5GneZ9uU1yzIuPuujKE0LSSc3eGu2IPfeBYoytBrtj1SUtKvVx0P+JmiKkVr5w==" /></div>
            <button class="octicon-btn octicon-btn-danger tooltipped tooltipped-n" type="submit" aria-label="Fork this project and delete file" data-disable-with>
              <span class="octicon octicon-trashcan"></span>
            </button>
</form>    </div>

    <div class="file-info">
        241 lines (222 sloc)
        <span class="file-info-divider"></span>
      9.677 kb
    </div>
  </div>
  
  <div class="blob-wrapper data type-python">
      <table class="highlight tab-size-8 js-file-line-container">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code js-file-line"><span class="pl-c"># Skeleton Program code for the AQA COMP1 Summer 2015 examination</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code js-file-line"><span class="pl-c"># this code should be used in conjunction with the Preliminary Material</span></td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code js-file-line"><span class="pl-c"># written by the AQA COMP1 Programmer Team</span></td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code js-file-line"><span class="pl-c"># developed in the Python 3.4 programming environment</span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code js-file-line">BOARDDIMENSION <span class="pl-k">=</span> <span class="pl-c1">8</span></td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">CreateBoard</span>():</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code js-file-line">  Board <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code js-file-line">  <span class="pl-k">for</span> Count <span class="pl-k">in</span> <span class="pl-c1">range</span>(BOARDDIMENSION <span class="pl-k">+</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code js-file-line">    Board.append([])</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code js-file-line">    <span class="pl-k">for</span> Count2 <span class="pl-k">in</span> <span class="pl-c1">range</span>(BOARDDIMENSION <span class="pl-k">+</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code js-file-line">      Board[Count].append(<span class="pl-s"><span class="pl-pds">&quot;</span>  <span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code js-file-line">  <span class="pl-k">return</span> Board</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">DisplayWhoseTurnItIs</span>(<span class="pl-smi">WhoseTurn</span>):</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code js-file-line">  <span class="pl-k">if</span> WhoseTurn <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>W<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code js-file-line">    <span class="pl-k">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>It is White&#39;s turn<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code js-file-line">  <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code js-file-line">    <span class="pl-k">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>It is Black&#39;s turn<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">GetTypeOfGame</span>():</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code js-file-line">  TypeOfGame <span class="pl-k">=</span> <span class="pl-c1">input</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Do you want to play the sample game (enter Y for Yes)? <span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code js-file-line">  <span class="pl-k">return</span> TypeOfGame</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">DisplayWinner</span>(<span class="pl-smi">WhoseTurn</span>):</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code js-file-line">  <span class="pl-k">if</span> WhoseTurn <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>W<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code js-file-line">    <span class="pl-k">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Black&#39;s Sarrum has been captured.  White wins!<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code js-file-line">  <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code js-file-line">    <span class="pl-k">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>White&#39;s Sarrum has been captured.  Black wins!<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">CheckIfGameWillBeWon</span>(<span class="pl-smi">Board</span>, <span class="pl-smi">FinishRank</span>, <span class="pl-smi">FinishFile</span>):</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code js-file-line">  <span class="pl-k">if</span> Board[FinishRank][FinishFile][<span class="pl-c1">1</span>] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>S<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code js-file-line">    <span class="pl-k">return</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code js-file-line">  <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code js-file-line">    <span class="pl-k">return</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">DisplayBoard</span>(<span class="pl-smi">Board</span>):</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code js-file-line">  <span class="pl-k">print</span>()</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code js-file-line">  <span class="pl-k">for</span> RankNo <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">1</span>, BOARDDIMENSION <span class="pl-k">+</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code js-file-line">    <span class="pl-k">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>     _______________________<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code js-file-line">    <span class="pl-k">print</span>(RankNo, end<span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>   <span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code js-file-line">    <span class="pl-k">for</span> FileNo <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">1</span>, BOARDDIMENSION <span class="pl-k">+</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code js-file-line">      <span class="pl-k">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>|<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> Board[RankNo][FileNo], end<span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code js-file-line">    <span class="pl-k">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>|<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code js-file-line">  <span class="pl-k">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>     _______________________<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code js-file-line">  <span class="pl-k">print</span>()</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code js-file-line">  <span class="pl-k">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>      1  2  3  4  5  6  7  8<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code js-file-line">  <span class="pl-k">print</span>()</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code js-file-line">  <span class="pl-k">print</span>()    </td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">CheckRedumMoveIsLegal</span>(<span class="pl-smi">Board</span>, <span class="pl-smi">StartRank</span>, <span class="pl-smi">StartFile</span>, <span class="pl-smi">FinishRank</span>, <span class="pl-smi">FinishFile</span>, <span class="pl-smi">ColourOfPiece</span>):</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code js-file-line">  CheckRedumMoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code js-file-line">  <span class="pl-k">if</span> ColourOfPiece <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>W<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code js-file-line">    <span class="pl-k">if</span> FinishRank <span class="pl-k">==</span> StartRank <span class="pl-k">-</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code js-file-line">      <span class="pl-k">if</span> FinishFile <span class="pl-k">==</span> StartFile <span class="pl-k">and</span> Board[FinishRank][FinishFile] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>  <span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code js-file-line">        CheckRedumMoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code js-file-line">      <span class="pl-k">elif</span> <span class="pl-c1">abs</span>(FinishFile <span class="pl-k">-</span> StartFile) <span class="pl-k">==</span> <span class="pl-c1">1</span> <span class="pl-k">and</span> Board[FinishRank][FinishFile][<span class="pl-c1">0</span>] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>B<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code js-file-line">        CheckRedumMoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code js-file-line">  <span class="pl-k">elif</span> FinishRank <span class="pl-k">==</span> StartRank <span class="pl-k">+</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code js-file-line">    <span class="pl-k">if</span> FinishFile <span class="pl-k">==</span> StartFile <span class="pl-k">and</span> Board[FinishRank][FinishFile] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>  <span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code js-file-line">      CheckRedumMoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code js-file-line">    <span class="pl-k">elif</span> <span class="pl-c1">abs</span>(FinishFile <span class="pl-k">-</span> StartFile) <span class="pl-k">==</span> <span class="pl-c1">1</span> <span class="pl-k">and</span> Board[FinishRank][FinishFile][<span class="pl-c1">0</span>] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>W<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code js-file-line">      CheckRedumMoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code js-file-line">  <span class="pl-k">return</span> CheckRedumMoveIsLegal</td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">CheckSarrumMoveIsLegal</span>(<span class="pl-smi">Board</span>, <span class="pl-smi">StartRank</span>, <span class="pl-smi">StartFile</span>, <span class="pl-smi">FinishRank</span>, <span class="pl-smi">FinishFile</span>):</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code js-file-line">  CheckSarrumMoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">abs</span>(FinishFile <span class="pl-k">-</span> StartFile) <span class="pl-k">&lt;=</span> <span class="pl-c1">1</span> <span class="pl-k">and</span> <span class="pl-c1">abs</span>(FinishRank <span class="pl-k">-</span> StartRank) <span class="pl-k">&lt;=</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code js-file-line">    CheckSarrumMoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code js-file-line">  <span class="pl-k">return</span> CheckSarrumMoveIsLegal</td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">CheckGisgigirMoveIsLegal</span>(<span class="pl-smi">Board</span>, <span class="pl-smi">StartRank</span>, <span class="pl-smi">StartFile</span>, <span class="pl-smi">FinishRank</span>, <span class="pl-smi">FinishFile</span>):</td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code js-file-line">  GisgigirMoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code js-file-line">  RankDifference <span class="pl-k">=</span> FinishRank <span class="pl-k">-</span> StartRank</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code js-file-line">  FileDifference <span class="pl-k">=</span> FinishFile <span class="pl-k">-</span> StartFile</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code js-file-line">  <span class="pl-k">if</span> RankDifference <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code js-file-line">    <span class="pl-k">if</span> FileDifference <span class="pl-k">&gt;=</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code js-file-line">      GisgigirMoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code js-file-line">      <span class="pl-k">for</span> Count <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">1</span>, FileDifference):</td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code js-file-line">        <span class="pl-k">if</span> Board[StartRank][StartFile <span class="pl-k">+</span> Count] <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>  <span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code js-file-line">          GisgigirMoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code js-file-line">    <span class="pl-k">elif</span> FileDifference <span class="pl-k">&lt;=</span> <span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code js-file-line">      GisgigirMoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code js-file-line">      <span class="pl-k">for</span> Count <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-k">-</span><span class="pl-c1">1</span>, FileDifference, <span class="pl-k">-</span><span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code js-file-line">        <span class="pl-k">if</span> Board[StartRank][StartFile <span class="pl-k">+</span> Count] <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>  <span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code js-file-line">          GisgigirMoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code js-file-line">  <span class="pl-k">elif</span> FileDifference <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code js-file-line">    <span class="pl-k">if</span> RankDifference <span class="pl-k">&gt;=</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code js-file-line">      GisgigirMoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code js-file-line">      <span class="pl-k">for</span> Count <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">1</span>, RankDifference):</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code js-file-line">        <span class="pl-k">if</span> Board[StartRank <span class="pl-k">+</span> Count][StartFile] <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>  <span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code js-file-line">          GisgigirMoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code js-file-line">    <span class="pl-k">elif</span> RankDifference <span class="pl-k">&lt;=</span> <span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code js-file-line">      GisgigirMoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code js-file-line">      <span class="pl-k">for</span> Count <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-k">-</span><span class="pl-c1">1</span>, RankDifference, <span class="pl-k">-</span><span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code js-file-line">        <span class="pl-k">if</span> Board[StartRank <span class="pl-k">+</span> Count][StartFile] <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>  <span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code js-file-line">          GisgigirMoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code js-file-line">  <span class="pl-k">return</span> GisgigirMoveIsLegal</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">CheckNabuMoveIsLegal</span>(<span class="pl-smi">Board</span>, <span class="pl-smi">StartRank</span>, <span class="pl-smi">StartFile</span>, <span class="pl-smi">FinishRank</span>, <span class="pl-smi">FinishFile</span>):</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code js-file-line">  CheckNabuMoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">abs</span>(FinishFile <span class="pl-k">-</span> StartFile) <span class="pl-k">==</span> <span class="pl-c1">1</span> <span class="pl-k">and</span> <span class="pl-c1">abs</span>(FinishRank <span class="pl-k">-</span> StartRank) <span class="pl-k">==</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code js-file-line">    CheckNabuMoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code js-file-line">  <span class="pl-k">return</span> CheckNabuMoveIsLegal</td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">CheckMarzazPaniMoveIsLegal</span>(<span class="pl-smi">Board</span>, <span class="pl-smi">StartRank</span>, <span class="pl-smi">StartFile</span>, <span class="pl-smi">FinishRank</span>, <span class="pl-smi">FinishFile</span>):</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code js-file-line">  CheckMarzazPaniMoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code js-file-line">  <span class="pl-k">if</span> (<span class="pl-c1">abs</span>(FinishFile <span class="pl-k">-</span> StartFile) <span class="pl-k">==</span> <span class="pl-c1">1</span> <span class="pl-k">and</span> <span class="pl-c1">abs</span>(FinishRank <span class="pl-k">-</span> StartRank) <span class="pl-k">==</span> <span class="pl-c1">0</span>) <span class="pl-k">or</span> (<span class="pl-c1">abs</span>(FinishFile <span class="pl-k">-</span> StartFile) <span class="pl-k">==</span> <span class="pl-c1">0</span> <span class="pl-k">and</span> <span class="pl-c1">abs</span>(FinishRank <span class="pl-k">-</span> StartRank) <span class="pl-k">==</span><span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code js-file-line">    CheckMarzazPaniMoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code js-file-line">  <span class="pl-k">return</span> CheckMarzazPaniMoveIsLegal</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">CheckEtluMoveIsLegal</span>(<span class="pl-smi">Board</span>, <span class="pl-smi">StartRank</span>, <span class="pl-smi">StartFile</span>, <span class="pl-smi">FinishRank</span>, <span class="pl-smi">FinishFile</span>):</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code js-file-line">  CheckEtluMoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code js-file-line">  <span class="pl-k">if</span> (<span class="pl-c1">abs</span>(FinishFile <span class="pl-k">-</span> StartFile) <span class="pl-k">==</span> <span class="pl-c1">2</span> <span class="pl-k">and</span> <span class="pl-c1">abs</span>(FinishRank <span class="pl-k">-</span> StartRank) <span class="pl-k">==</span> <span class="pl-c1">0</span>) <span class="pl-k">or</span> (<span class="pl-c1">abs</span>(FinishFile <span class="pl-k">-</span> StartFile) <span class="pl-k">==</span> <span class="pl-c1">0</span> <span class="pl-k">and</span> <span class="pl-c1">abs</span>(FinishRank <span class="pl-k">-</span> StartRank) <span class="pl-k">==</span> <span class="pl-c1">2</span>):</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code js-file-line">    CheckEtluMoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code js-file-line">  <span class="pl-k">return</span> CheckEtluMoveIsLegal</td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">CheckMoveIsLegal</span>(<span class="pl-smi">Board</span>, <span class="pl-smi">StartRank</span>, <span class="pl-smi">StartFile</span>, <span class="pl-smi">FinishRank</span>, <span class="pl-smi">FinishFile</span>, <span class="pl-smi">WhoseTurn</span>):</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code js-file-line">  MoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code js-file-line">  <span class="pl-k">if</span> (FinishFile <span class="pl-k">==</span> StartFile) <span class="pl-k">and</span> (FinishRank <span class="pl-k">==</span> StartRank):</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code js-file-line">    MoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code js-file-line">  <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code js-file-line">    PieceType <span class="pl-k">=</span> Board[StartRank][StartFile][<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code js-file-line">    PieceColour <span class="pl-k">=</span> Board[StartRank][StartFile][<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code js-file-line">    <span class="pl-k">if</span> WhoseTurn <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>W<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code js-file-line">      <span class="pl-k">if</span> PieceColour <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>W<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code js-file-line">        MoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code js-file-line">      <span class="pl-k">if</span> Board[FinishRank][FinishFile][<span class="pl-c1">0</span>] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>W<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code js-file-line">        MoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code js-file-line">      <span class="pl-k">if</span> PieceColour <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>B<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code js-file-line">        MoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code js-file-line">      <span class="pl-k">if</span> Board[FinishRank][FinishFile][<span class="pl-c1">0</span>] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>B<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code js-file-line">        MoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code js-file-line">    <span class="pl-k">if</span> MoveIsLegal <span class="pl-k">==</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code js-file-line">      <span class="pl-k">if</span> PieceType <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>R<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code js-file-line">        MoveIsLegal <span class="pl-k">=</span> CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, PieceColour)</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code js-file-line">      <span class="pl-k">elif</span> PieceType <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>S<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code js-file-line">        MoveIsLegal <span class="pl-k">=</span> CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)</td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code js-file-line">      <span class="pl-k">elif</span> PieceType <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>M<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code js-file-line">        MoveIsLegal <span class="pl-k">=</span> CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)</td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code js-file-line">      <span class="pl-k">elif</span> PieceType <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>G<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code js-file-line">        MoveIsLegal <span class="pl-k">=</span> CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code js-file-line">      <span class="pl-k">elif</span> PieceType <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>N<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code js-file-line">        MoveIsLegal <span class="pl-k">=</span> CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code js-file-line">      <span class="pl-k">elif</span> PieceType <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>E<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code js-file-line">        MoveIsLegal <span class="pl-k">=</span> CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)</td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code js-file-line">  <span class="pl-k">return</span> MoveIsLegal</td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">InitialiseBoard</span>(<span class="pl-smi">Board</span>, <span class="pl-smi">SampleGame</span>):</td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code js-file-line">  <span class="pl-k">if</span> SampleGame <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Y<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code js-file-line">    <span class="pl-k">for</span> RankNo <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">1</span>, BOARDDIMENSION <span class="pl-k">+</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code js-file-line">      <span class="pl-k">for</span> FileNo <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">1</span>, BOARDDIMENSION <span class="pl-k">+</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code js-file-line">        Board[RankNo][FileNo] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>  <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code js-file-line">    Board[<span class="pl-c1">1</span>][<span class="pl-c1">2</span>] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>BG<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code js-file-line">    Board[<span class="pl-c1">1</span>][<span class="pl-c1">4</span>] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>BS<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code js-file-line">    Board[<span class="pl-c1">1</span>][<span class="pl-c1">8</span>] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>WG<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code js-file-line">    Board[<span class="pl-c1">2</span>][<span class="pl-c1">1</span>] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>WR<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code js-file-line">    Board[<span class="pl-c1">3</span>][<span class="pl-c1">1</span>] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>WS<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code js-file-line">    Board[<span class="pl-c1">3</span>][<span class="pl-c1">2</span>] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>BE<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code js-file-line">    Board[<span class="pl-c1">3</span>][<span class="pl-c1">8</span>] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>BE<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code js-file-line">    Board[<span class="pl-c1">6</span>][<span class="pl-c1">8</span>] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>BR<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code js-file-line">  <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code js-file-line">    <span class="pl-k">for</span> RankNo <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">1</span>, BOARDDIMENSION <span class="pl-k">+</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code js-file-line">      <span class="pl-k">for</span> FileNo <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">1</span>, BOARDDIMENSION <span class="pl-k">+</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code js-file-line">        <span class="pl-k">if</span> RankNo <span class="pl-k">==</span> <span class="pl-c1">2</span>:</td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code js-file-line">          Board[RankNo][FileNo] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>BR<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code js-file-line">        <span class="pl-k">elif</span> RankNo <span class="pl-k">==</span> <span class="pl-c1">7</span>:</td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code js-file-line">          Board[RankNo][FileNo] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>WR<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code js-file-line">        <span class="pl-k">elif</span> RankNo <span class="pl-k">==</span> <span class="pl-c1">1</span> <span class="pl-k">or</span> RankNo <span class="pl-k">==</span> <span class="pl-c1">8</span>:</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code js-file-line">          <span class="pl-k">if</span> RankNo <span class="pl-k">==</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code js-file-line">            Board[RankNo][FileNo] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>B<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code js-file-line">          <span class="pl-k">if</span> RankNo <span class="pl-k">==</span> <span class="pl-c1">8</span>:</td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code js-file-line">            Board[RankNo][FileNo] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>W<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code js-file-line">          <span class="pl-k">if</span> FileNo <span class="pl-k">==</span> <span class="pl-c1">1</span> <span class="pl-k">or</span> FileNo <span class="pl-k">==</span> <span class="pl-c1">8</span>:</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code js-file-line">            Board[RankNo][FileNo] <span class="pl-k">=</span> Board[RankNo][FileNo] <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>G<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code js-file-line">          <span class="pl-k">elif</span> FileNo <span class="pl-k">==</span> <span class="pl-c1">2</span> <span class="pl-k">or</span> FileNo <span class="pl-k">==</span> <span class="pl-c1">7</span>:</td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code js-file-line">            Board[RankNo][FileNo] <span class="pl-k">=</span> Board[RankNo][FileNo] <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>E<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code js-file-line">          <span class="pl-k">elif</span> FileNo <span class="pl-k">==</span> <span class="pl-c1">3</span> <span class="pl-k">or</span> FileNo <span class="pl-k">==</span> <span class="pl-c1">6</span>:</td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code js-file-line">            Board[RankNo][FileNo] <span class="pl-k">=</span> Board[RankNo][FileNo] <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>N<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code js-file-line">          <span class="pl-k">elif</span> FileNo <span class="pl-k">==</span> <span class="pl-c1">4</span>:</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code js-file-line">            Board[RankNo][FileNo] <span class="pl-k">=</span> Board[RankNo][FileNo] <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>M<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code js-file-line">          <span class="pl-k">elif</span> FileNo <span class="pl-k">==</span> <span class="pl-c1">5</span>:</td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code js-file-line">            Board[RankNo][FileNo] <span class="pl-k">=</span> Board[RankNo][FileNo] <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>S<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code js-file-line">          Board[RankNo][FileNo] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>  <span class="pl-pds">&quot;</span></span>    </td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code js-file-line">                    </td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">GetMove</span>(<span class="pl-smi">StartSquare</span>, <span class="pl-smi">FinishSquare</span>):</td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code js-file-line">  StartSquare <span class="pl-k">=</span> <span class="pl-c1">int</span>(<span class="pl-c1">input</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Enter coordinates of square containing piece to move (file first): <span class="pl-pds">&quot;</span></span>))</td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code js-file-line">  FinishSquare <span class="pl-k">=</span> <span class="pl-c1">int</span>(<span class="pl-c1">input</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Enter coordinates of square to move piece to (file first): <span class="pl-pds">&quot;</span></span>))</td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code js-file-line">  <span class="pl-k">return</span> StartSquare, FinishSquare</td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">MakeMove</span>(<span class="pl-smi">Board</span>, <span class="pl-smi">StartRank</span>, <span class="pl-smi">StartFile</span>, <span class="pl-smi">FinishRank</span>, <span class="pl-smi">FinishFile</span>, <span class="pl-smi">WhoseTurn</span>):</td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code js-file-line">  <span class="pl-k">if</span> WhoseTurn <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>W<span class="pl-pds">&quot;</span></span> <span class="pl-k">and</span> FinishRank <span class="pl-k">==</span> <span class="pl-c1">1</span> <span class="pl-k">and</span> Board[StartRank][StartFile][<span class="pl-c1">1</span>] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>R<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code js-file-line">    Board[FinishRank][FinishFile] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>WM<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code js-file-line">    Board[StartRank][StartFile] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>  <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code js-file-line">  <span class="pl-k">elif</span> WhoseTurn <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>B<span class="pl-pds">&quot;</span></span> <span class="pl-k">and</span> FinishRank <span class="pl-k">==</span> <span class="pl-c1">8</span> <span class="pl-k">and</span> Board[StartRank][StartFile][<span class="pl-c1">1</span>] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>R<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code js-file-line">    Board[FinishRank][FinishFile] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>BM<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code js-file-line">    Board[StartRank][StartFile] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>  <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code js-file-line">  <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code js-file-line">    Board[FinishRank][FinishFile] <span class="pl-k">=</span> Board[StartRank][StartFile]</td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code js-file-line">    Board[StartRank][StartFile] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>  <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code js-file-line"><span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>__main__<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code js-file-line">  Board <span class="pl-k">=</span> CreateBoard() <span class="pl-c">#0th index not used</span></td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code js-file-line">  StartSquare <span class="pl-k">=</span> <span class="pl-c1">0</span> </td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code js-file-line">  FinishSquare <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code js-file-line">  PlayAgain <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Y<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code js-file-line">  <span class="pl-k">while</span> PlayAgain <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Y<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code js-file-line">    WhoseTurn <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>W<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code js-file-line">    GameOver <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code js-file-line">    SampleGame <span class="pl-k">=</span> <span class="pl-c1">input</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Do you want to play the sample game (enter Y for Yes)? <span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">ord</span>(SampleGame) <span class="pl-k">&gt;=</span> <span class="pl-c1">97</span> <span class="pl-k">and</span> <span class="pl-c1">ord</span>(SampleGame) <span class="pl-k">&lt;=</span> <span class="pl-c1">122</span>:</td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code js-file-line">      SampleGame <span class="pl-k">=</span> <span class="pl-c1">chr</span>(<span class="pl-c1">ord</span>(SampleGame) <span class="pl-k">-</span> <span class="pl-c1">32</span>)</td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code js-file-line">    InitialiseBoard(Board, SampleGame)</td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code js-file-line">    <span class="pl-k">while</span> <span class="pl-k">not</span>(GameOver):</td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code js-file-line">      DisplayBoard(Board)</td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code js-file-line">      DisplayWhoseTurnItIs(WhoseTurn)</td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code js-file-line">      MoveIsLegal <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code js-file-line">      <span class="pl-k">while</span> <span class="pl-k">not</span>(MoveIsLegal):</td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code js-file-line">        StartSquare, FinishSquare <span class="pl-k">=</span> GetMove(StartSquare, FinishSquare)</td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code js-file-line">        StartRank <span class="pl-k">=</span> StartSquare <span class="pl-k">%</span> <span class="pl-c1">10</span></td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code js-file-line">        StartFile <span class="pl-k">=</span> StartSquare <span class="pl-k">//</span> <span class="pl-c1">10</span></td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code js-file-line">        FinishRank <span class="pl-k">=</span> FinishSquare <span class="pl-k">%</span> <span class="pl-c1">10</span></td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code js-file-line">        FinishFile <span class="pl-k">=</span> FinishSquare <span class="pl-k">//</span> <span class="pl-c1">10</span></td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code js-file-line">        MoveIsLegal <span class="pl-k">=</span> CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)</td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span>(MoveIsLegal):</td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code js-file-line">          <span class="pl-k">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>That is not a legal move - please try again<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code js-file-line">      GameOver <span class="pl-k">=</span> CheckIfGameWillBeWon(Board, FinishRank, FinishFile)</td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code js-file-line">      MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)</td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code js-file-line">      <span class="pl-k">if</span> GameOver:</td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code js-file-line">        DisplayWinner(WhoseTurn)</td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code js-file-line">      <span class="pl-k">if</span> WhoseTurn <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>W<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code js-file-line">        WhoseTurn <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>B<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code js-file-line">      <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code js-file-line">        WhoseTurn <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>W<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code js-file-line">    PlayAgain <span class="pl-k">=</span> <span class="pl-c1">input</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Do you want to play again (enter Y for Yes)? <span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">ord</span>(PlayAgain) <span class="pl-k">&gt;=</span> <span class="pl-c1">97</span> <span class="pl-k">and</span> <span class="pl-c1">ord</span>(PlayAgain) <span class="pl-k">&lt;=</span> <span class="pl-c1">122</span>:</td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code js-file-line">      PlayAgain <span class="pl-k">=</span> <span class="pl-c1">chr</span>(<span class="pl-c1">ord</span>(PlayAgain) <span class="pl-k">-</span> <span class="pl-c1">32</span>)</td>
      </tr>
</table>

  </div>

</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="btn">Go</button>
</form></div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2015 <span title="0.06131s from github-fe129-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact</a></li>
    </ul>
  </div>
</div>


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-suggester-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents" placeholder=""></textarea>
      <div class="suggester-container">
        <div class="suggester fullscreen-suggester js-suggester js-navigation-container"></div>
      </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    
    

    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x flash-close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-d22b59d0085e83b7549ba4341ec9e68f80c2f29c8e49213ee182003dc8d568c6.js"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-504dff3e8e0e391a1b545db0b1d117e086a912948fd385da44a23112ae1063a4.js"></script>
      
      

  </body>
</html>

