/* manually minified; use a beautifier like http://jsbeautifier.org/ to unpack */
(function(){container={sections:{},viewed:{},max:{},useClass:false,prefix:".",locURL:"",urlHash:"",scrollcheck:function(){jQuery(document).ready(function(){var e=getWebtrendsWtEsString();if(e.charAt(e.length-1)==="/"){e=e.substring(0,e.length-1)}container.locURL=e;container.urlHash=window.location.hash;container.prefix=container.useClass?".":"#";for(section in container.sections){for(element in container.sections[section]){if(typeof $(container.prefix+element).attr("href")!="undefined"){href=$(container.prefix+element).attr("href");href=href.indexOf("?")>=0?href+"&":href+"?";$(container.prefix+element).attr("href",href+"WT.adsec="+section)}}container.viewed[section]=false;container.max[section]=0}container.assignSections();$(window).on("scroll",function(){container.checkImpressions()});$(window).resize(function(){container.assignSections();container.checkImpressions()});container.checkImpressions()})},assignSections:function(){for(section in container.sections){for(element in container.sections[section]){currH=0;currH=$(container.prefix+element).height()/2+$(container.prefix+element).offset().top;if(currH>container.max[section])container.max[section]=currH}}},checkImpressions:function(){if(container.urlHash!==window.location.hash){container.urlHash=window.location.hash;return}if($("html, body").is(":animated")){return}var e="innerHeight"in window?window.innerHeight:document.compatMode!=="BackCompat"?document.documentElement.clientHeight:document.body.clientHeight;var t=$(window).scrollTop();current=t+e;for(section in container.sections){if(!container.viewed[section]){if(current>container.max[section]&&container.max[section]>t){container.viewed[section]=true;elms="";for(elm in container.sections[section]){elms+=container.sections[section][elm]+";"}elms=elms.slice(0,-1);Webtrends.multiTrack({argsa:["WT.dl","0","WT.z_sec",section,"WT.es",container.locURL+"/"+section+".sec"]})}}}for(var n in Webtrends.dcss){var r=Webtrends.dcss[n];r.WT["z_sec"]=""}},dowork:function(e,t){var r=false;for(n in t){if(n=="src"||n=="loaded"){}else if("trackableidsclass"){$("."+t[n]).each(function(e){if($(this).attr("id")){var t=$(this).attr("id");var n={};n[t]=t;container.sections[t]=n;r=true}})}else{container.sections[n]=t[n];r=true}}if(r){container.scrollcheck()}}}})();Webtrends.registerPlugin("sectionImpression",container.dowork)