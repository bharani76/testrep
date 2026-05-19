# Instagram Viral Agent Setup Guide

To use the automated publishing feature, you need to obtain an Instagram Graph API Token and your Instagram User ID. Follow these steps:

## Prerequisites
1. **Instagram Business/Creator Account**: In your Instagram app, go to Settings -> Account Type and Tools -> Switch to Professional Account.
2. **Linked Facebook Page**: Your Instagram Professional account must be linked to a Facebook Page you manage.

---

## Step 1: Create a Meta Developer App
1. Go to the [Meta for Developers](https://developers.facebook.com/) portal.
2. Click **My Apps** -> **Create App**.
3. Select **Other** for app type, then **Business**.
4. Give your app a name and click **Create App**.

## Step 2: Add Instagram Graph API
1. In your App Dashboard, scroll down to **Add a product**.
2. Find **Instagram Graph API** and click **Set up**.

## Step 3: Generate an Access Token
1. Go to the [Graph API Explorer](https://developers.facebook.com/tools/explorer/).
2. Select your App in the top right dropdown.
3. In the **User or Page** dropdown, select **Get User Access Token**.
4. Under **Permissions**, add:
   - `instagram_basic`
   - `instagram_content_publish`
   - `pages_show_list`
   - `pages_read_engagement`
5. Click **Generate Access Token**. Log in and select the Facebook Page linked to your Instagram.
6. Copy the **Access Token**.

## Step 4: Get your Instagram User ID
1. In the Graph API Explorer, use the following query (replace `me` with your Page ID if needed):
   `GET /v25.0/me/accounts?fields=instagram_business_account`
2. Run the query. You will see an `instagram_business_account` object.
3. The `id` inside that object is your **IG_USER_ID**.

## Step 5: Extend to a Long-Lived Token (60 days)
1. Go to the [Access Token Tool](https://developers.facebook.com/tools/accesstoken/).
2. Find your token and click **Debug**.
3. Click **Extend Access Token** at the bottom.
4. Copy the new long-lived token.

## Step 6: Configure .env
Create a `.env` file in the project root (use `.env.example` as a template):
```env
HUGGINGFACE_API_KEY=your_key
IG_USER_ID=your_id_from_step_4
IG_ACCESS_TOKEN=your_token_from_step_5
DRY_RUN=False
```

## Step 7: Run the Agent
1. Start the scheduler: `python scheduler_service.py`
2. Start the dashboard: `python dashboard.py`
3. Check your posts at `http://localhost:5000`
