---
title: "How to have a self bolt.new programming tool -all free tool,use cloudlfare,huggingface,github "
meta_title: ""
description: "learn how to setup cloudflare host self bot.new to utilize germini flash model"
date: 2025-01-05T22:18:12Z
image: "/images/image-placeholder.png"
categories: ["工作"]
author: "haisheng"
tags: ["bolt.new","cursor",'winsurf',"germini flash"]
draft: false
---




currently i use google studio, but it need a lot copy and paste work to see code if working

https://aistudio.google.com/prompts/1SPaafTGDjLUn_zDuDuOviig9MaUcfr94



> Last Updated: 4:44 PM 01/03/2025

**Let’s dive right in!**

There are some dependencies needed to get [**Bolt.diy⚡** 55](https://bolt.diy) running on your local machine.

These are also generally required for building and deployment, but this tutorial will be so EASY, we are going to skip all that noise 


We are going to use GitHub Actions to build everything in the cloud 

And the best part? **Bolt.diy** already has mostly everything you need setup for you, with some minor adjustments (basically need to remove a few things and set some flags).

**No** need to install the latest .NET version (can be an issue on Windows), have Node (npm and pnpm), or even Git. No needing to deal with security 
or any type of setup.
That’s how easy this is going to be. So, follow all steps closely and let’s see who gets to the finish line first!

**Prerequisites**: There are only three; 
sign up account if you do not already have them. 
* a [Cloudflare 56](https://dash.cloudflare.com/sign-up) 

* [GitHub 18](https://github.com/signup)

* and [HuggingFace 46](https://huggingface.co/settings/tokens)


They are all completely **FREE**!

**Setting up GitHub 

1.  Browse to the GitHub page and sign in, or create an account.
    
2.  Browse to the [Bolt.diy GitHub Page 184](https://github.com/coleam00/bolt.new-any-llm)
    
3.  Click Fork
    
    ![image](https://thinktank.ottomator.ai/uploads/db4962/optimized/2X/e/e0c3652624a7ab31afa4b93407350d6c84279fbf_2_690x181.png)
    
    
    
5.  In the “Create a new fork” dialog, click the “Create fork” button  
    
    ![image](https://thinktank.ottomator.ai/uploads/db4962/optimized/2X/a/a13a487337428af3b4366641b01e4c3dcf168bd0_2_487x375.png)
    
    
    
      
    **Note:** Do not check "Copy the `main` branch only, so we have the ability to switch them later (update). And while you could just sync the `stable` branch, it’s probably best to pull all of them for the flexibility (for example if you need, or want, to change branches later).
    
6.  A little bit of waiting…  
    ![image](https://thinktank.ottomator.ai/uploads/db4962/original/2X/c/c65d48217668e4221cbef828d6b98cfbba3d80c4.png)
    
7.  Click “Code” and browse to “.tool-verions”  
    
    ![image](https://thinktank.ottomator.ai/uploads/db4962/optimized/2X/f/f9777251fb8d42efe759b298d1afda67a7dfa1e1_2_690x39.png)
    
    
    
8.  Switch to the `stable` branch from the drop-down.  
    **Note:** in version 0.0.3 Bolt.diy was changed to have a `stable` branch because `main` is what PR’s are committed and resolve to.
    
9.  Click on the `.tool-version` filename to open it and delete the file.  
    
    ![image](https://thinktank.ottomator.ai/uploads/db4962/optimized/2X/4/4c195432966e57172273c3fad920cd92877dcfb6_2_690x294.png)
    
    
    
      
    **Notes:** this file causes issues with the deployment.
    
10.  Commit the Changes back to your Fork:  
    
    ![image](https://thinktank.ottomator.ai/uploads/db4962/optimized/2X/3/331561d1cc0618b3263041f2354a9f62a25abe8c_2_676x500.png)
    
    
    
11.  Do the same for the `wrangler.toml`  
    
    ![image](https://thinktank.ottomator.ai/uploads/db4962/optimized/2X/2/23243eeb0717d0ad638875e8a96f47042d2a2e49_2_690x298.png)
    
    
    
      
    
    ![image](https://thinktank.ottomator.ai/uploads/db4962/optimized/2X/f/f550b300f544620175483a00512d20024d1992c9_2_477x500.png)
    
    
    
      
    **Note:** Because otherwise Cloudflare will detect it, use it to deploy, and then overwrite the environment variables when we move onto the Cloudflare setup. If you want to deploy without keys, that’s perfectly fine, just note that Bolt.diy does a periodic check whether or not they are set and without them it may not work (not sure if this was changed in the most recent merge). Alternatively, if you used git to clone the repo locally, you could just rename them (but that means more steps).
    

**Setting up Cloudflare⚙️**

1.  Sign up for, or login to, Cloudflare.
    
2.  In Cloudflare click on “Workers & Pages”  
    ![image](https://thinktank.ottomator.ai/uploads/db4962/original/2X/9/90a0280dddb10bc250752f9234234502fbcfc320.png)
    
3.  Click “Create”  
    
  ![image](https://thinktank.ottomator.ai/uploads/db4962/optimized/2X/8/816438ce3fb27da2fe69211a5327d4360350df20_2_690x145.png)
    
    
    
5.  Click on “Pages” tab and then “Connect to Git”  
    
    
![image](https://thinktank.ottomator.ai/uploads/db4962/optimized/2X/0/0173cf5f6064f4aa01fbd3b84efb4dadcf6746f9_2_690x422.png)
    
    
    
      
    **Note:** If this is the first time connecting git, Cloudflare will step you through the process and you will need to follow steps to authorize it.
    
7.  Select your GitHub account and Repository (bolt.diy)  
    
    ![image](https://thinktank.ottomator.ai/uploads/db4962/optimized/2X/0/0af637f63c16d98282e25497f5a62ba5a605ee78_2_560x500.png)
    
    
    
8.  Configure “Setup and Deploy” options:  
    a. For Framework preset, select `"Remix"` from the drop-down.  
    b. For Build command, we will be modifying this to be:  
    `npm install pnpm & pnpm install & pnpm run build`  
    **Note:** Add your environment variables exactly the way they are listed in your Environment Variables (.env file), see screenshot (you can open the _**.env.example**_ for reference). And **DO NOT** include the equals sign in the variable name as that’s intended as the separator between the variable and value (if you do, it will result in caching errors).  
      
    **WARNING: If you do not use `pnpm run build` (and leave the default `npm run build`), then the deployment will appear to work fine, but the page styling will be screwed up. If this happens, it’s fine as you can just modify the build command (and “Retry deployment”, see Steps #12-13) but if you run into a broken page, then you know why.**
    
9.  Click the “Setup and Deploy” button  
    
    
![image](https://thinktank.ottomator.ai/uploads/db4962/optimized/2X/c/cd65053542da0659a978a212c067f333d66a19bf_2_310x500.jpeg)
    
    
    
      
    **Note:** I did not include the keys in the image for security reasons, but make sure to add them here.
    
11.  Build failed (calm down, it’s fine! It’s fine!³)  
    
    
![image](https://thinktank.ottomator.ai/uploads/db4962/optimized/2X/d/d844d86fc4501f5506a99ef094e9b9ed2ced6acb_2_390x500.png)
    
    
    
      
    **Note:** we are not going to use wrangler and because of this the initial deployment will fail with error: `Error: Failed to publish your Function. Got error: Uncaught Error: No such module "node:process". imported from "functionsWorker-{cache_hash_key_value}.js"`  
    **Note:** In the newest version of Bolt.diy the build may not fail, but just confirm steps 8-10. It appears that something was changed to set the `nodejs_compat` compatibility flag.
    
11.  Click “Continue to project” and agree to the Warning Prompt:
    
![image](https://thinktank.ottomator.ai/uploads/db4962/original/2X/2/27bd4d394b2eceaa89b878e6aa2a41d23558ce07.png)
    
13.  Click Settings and scroll down to Runtime
    
![image](https://thinktank.ottomator.ai/uploads/db4962/optimized/2X/c/c4ed7ce2381fe3d5c67a499245d964954b286c9e_2_690x369.png)
    
    
    
      
    a. For “Compatibility date”, click edit, select `2024-09-02`, and click “Save”  
    ![image](https://thinktank.ottomator.ai/uploads/db4962/original/2X/6/6ee4b162eb6942b97bf499e77d6051f143e2bef5.png)  
    b. For “Compatability flags”, click edit, set to `nodejs_compat`, and click “Save”  
    **Note:** the option will not be in the drop-down list, you will need to type it in and select the “tag” for it.  
    ![image](https://thinktank.ottomator.ai/uploads/db4962/original/2X/1/110331884727a91ad2aa0bcc231ee95a89903c55.png)  
    c. When you are done, it should look like this:  
    
    ![image](https://thinktank.ottomator.ai/uploads/db4962/optimized/2X/c/cf4f7df0b757ff2c1f7d030feff2fbdc17846d73_2_345x123.png)
    
    
    
11.  On “Branch control”, click the edit icon (pen) and change branch to `stable`  
![image](https://thinktank.ottomator.ai/uploads/db4962/original/2X/4/400ba5134ab85ac0d08156a5dfd8e13b7dd38cd6.png)  
    **Note:** When the article was first written, there was no stable branch, but now this is the recommended branch to use.
    
12.  Click on the “Deployments” tab, then “View Details”:  
    
    ![image](https://thinktank.ottomator.ai/uploads/db4962/optimized/2X/a/a865a97b646a62e2d5a161865ebef431236e3544_2_690x272.png)
    
    
    
13.  Click “Retry deployment”  
    
    ![image](https://thinktank.ottomator.ai/uploads/db4962/optimized/2X/7/785a3cad763a258a741c17a55fa737c734f8a04b_2_690x176.png)
    
    
    
      
    **Note:** You could have “triggered” this process simply by modifying a file, committing the changes (or pushed them locally), and it would have re-deployed as well (see Step #14).
    
14.  Wait for it… Success! All Setup and Deployed!
    
    ![image](https://thinktank.ottomator.ai/uploads/db4962/optimized/2X/9/953c11598d316cd35013056bf3f31847e72517b9_2_495x499.png)
    
    
    
      
    **Note:** Due to caching, the page might not load correctly the first time. But don’t worry, if there are no warnings up to this point, let’s continue and give the changes a little time to propagate.
    
15.  Updating (Just an FIY – Nothing to do here!)
    **Notes:** The project is setup to activate GitHub Actions on Commit/Publish. We just need to modify a file to test it! This event would also be triggered if you did a Commit/Push the usual way on your local machine but we can also setup a schedule to do it for us. But that’s beyond the scope of this tutorial.  
    
    ![image](https://thinktank.ottomator.ai/uploads/db4962/optimized/2X/d/da2f3c3cfbf1bd747e4bfbec9bfb96fbeb1f3c02_2_690x479.png)
    
    
    
      
    a. Notice if you go back to “code”, the runner was activated!  
    
    ![image](https://thinktank.ottomator.ai/uploads/db4962/optimized/2X/0/00c0fef03312e75e43fab813eeeb1ed0fb494b03_2_690x301.png)
    
    
    
      
    b. Success on change.  
    
    ![image](https://thinktank.ottomator.ai/uploads/db4962/optimized/2X/5/52572a7bda177d8ab043d5615bcb59e3461267ca_2_689x368.png)
    
    
    
      
    c. Now you can sync the fork, but just remember to delete or blank out the `.tool-versions`, and `wrangler.toml` if they get re-created (not sure they will, I haven’t tested this yet).  
    
    ![image](https://thinktank.ottomator.ai/uploads/db4962/optimized/2X/7/72b66e7fdbe49e2b348318b7e271980158e8c4c5_2_690x48.png)
    
    
    
16.  Now lets check out our new deployment:  
    
    ![image](https://thinktank.ottomator.ai/uploads/db4962/optimized/2X/d/dd59d4ec68377cf0025e78fb0453a9878abd5a2d_2_690x257.png)
    
    
    
17.  It’s alive!!! It works, and it costed nothing but a little time!!
    
    ![image](https://thinktank.ottomator.ai/uploads/db4962/optimized/2X/8/82abedb6bd44edf8bc7c016e897c4b6e004f0d8a_2_690x388.jpeg)
    
    
    
      
    **`And now you have your own Bolt.diy to play with and share!`**
    

**Optional Steps:

**Setup a Custom URL

1.  If you already have a Domain name setup on Cloudflare, just provide the subdomain and the tool will take care of the rest for you (DNS records, etc.).  
    
    ![image](https://thinktank.ottomator.ai/uploads/db4962/optimized/2X/6/63bf21fb60f364bf41a0c0c90e1fe43efca97ae4_2_690x415.png)
    
    
    
2.  Let Cloudflare do the work and click “Activate domain”  
    
    ![image](https://thinktank.ottomator.ai/uploads/db4962/optimized/2X/4/4a1050a2b3bf25e2aa03d29bc5e0d13bc2b928f4_2_690x469.png)
    
    
    
3.  Wait a few minutes, and done.

**Updating Bolt.diy Deployment on Change**

1.  Go to your forked GitHub repo, change branch to “Stable” (or which ever one you are updating), and click the “Sync fork” dropdown"  
    
    ![image](https://thinktank.ottomator.ai/uploads/db4962/optimized/2X/b/bb81a7ea6557cb7511cd4a99cb5b4d01891da532_2_690x89.png)
    
    
    
2.  Click on “Update branch” in the dropdown:  
    **Note:** Do not click “Discard X commits” and then you don’t need to delete the `.tool-versions` and `wrangler.toml` files each time.  
    
    ![image](https://thinktank.ottomator.ai/uploads/db4962/optimized/2X/e/e3c24cce2ef3d5a897b682df57e21b2a91f2756c_2_188x250.png)
        
    
3.  Done.  
    Notice that updating the branch automatically trigger the Cloudflare Pages to re-build and deploy (there’s nothing else to do, just wait):  
    
    ![image](https://thinktank.ottomator.ai/uploads/db4962/optimized/2X/9/99dc61bb7264c041352ce61776c24778788e985b_2_690x55.png)
    
    
    
      
    
    ![image](https://thinktank.ottomator.ai/uploads/db4962/original/2X/9/97523bfc84c6759deb68381110f8759956db57df.png)
    
    
    
      
    **Note:** You can also setup a GitHub action to do this automatically and just keep the repo up to date on change, but I haven’t created documentation for this yet. It’s honestly not that hard either and just keeps me from having to do it manually (or even remembering to).
    

**TBD:**

*   User Authentication through [Cloudflare Zero Trust](https://thinktank.ottomator.ai/t/deploying-bolt-diy-with-cloudflare-pages-the-easy-way/2403/61)
*   Automatically update deployment through GitHub Actions.
*   Connecting Local Models (Ollama, LMStudio, etc.) to Cloudflare Pages Deployment
*   Integrating Supabase to Cloudflare Pages Deployment

**Troubleshooting:**

*   Bolt.diy [page styling is jacked up](https://thinktank.ottomator.ai/t/deploying-bolt-diy-with-cloudflare-pages-the-easy-way/2403/112), you get a module error, vite missing, then you used `npm install` at some point and/or did not update the build command. Check the instructions!
*   Error: `pnpm plugin is not installed`? You did not remove the `.tool-versions` and/or `wrangler.toml` from your forked repo. See comment [#108](https://thinktank.ottomator.ai/t/deploying-bolt-diy-with-cloudflare-pages-the-easy-way/2403/108)
*   There are some known issues with Safari that cause a bunch of cache errors. Try Chrome/Edge/Firefox. No known fix yet. See comment [#91](https://thinktank.ottomator.ai/t/deploying-bolt-diy-with-cloudflare-pages-the-easy-way/2403/91) and [#131](https://thinktank.ottomator.ai/t/deploying-bolt-diy-with-cloudflare-pages-the-easy-way/2403/131).
*   Error message after following guide? Likely did not change branch to `stable`. Check instructions for details and comment [#76](https://thinktank.ottomator.ai/t/deploying-bolt-diy-with-cloudflare-pages-the-easy-way/2403/76).
*   Want to secure your Cloudflare Pages Deployment down, see comment [#61](https://thinktank.ottomator.ai/t/deploying-bolt-diy-with-cloudflare-pages-the-easy-way/2403/61)
*   Make sure there are not equals signs in your environment variables
*   Make sure to set the compatability\_flags date and `nodejs_compat`
*   Ensure you are using the `stable` branch (see latest docs)

**Last Steps: Test your Deployment**

*   Open the URL (either generated or Custom) and test that everything works.
*   Please let me know if you run into issues and I can create a troubleshooting guide.
*   We would all appreciate you dropping an issue item through the [GitHub page 7](https://github.com/stackblitz-labs/bolt.diy), please just see if the issue already exists first.

**Final Thoughts 
This tutorial hopefully seems straight-forward but it took a lot of testing and process refining because there was really no good documentation on this. Hope it works for you, and you simply appreciate the effort (show some love – bookmark🔖 and give a heart❤️‍).

There will likely be updates to this tutorial in the future.

Thanks!

