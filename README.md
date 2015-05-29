# Happy Android Tools

A collection of tools for Android developers.

* layout-to-style
* ...

## [layout-to-style][]

A script to convert the layout attributes into style file format.

### Example

Input:

	<LinearLayout
		android:layout_width="match_parent"
		android:layout_height="wrap_content"
		android:layout_marginBottom="30dp"
		android:layout_marginTop="30dp"
		android:background="@color/transparent_white"
		android:orientation="vertical"
		android:paddingBottom="30dp"
		android:paddingTop="20dp">

Output:

	<style name="">
		<item name="android:layout_width">match_parent</item>
		<item name="android:layout_height">wrap_content</item>
		<item name="android:layout_marginBottom">30dp</item>
		<item name="android:layout_marginTop">30dp</item>
		<item name="android:background">@color/transparent_white</item>
		<item name="android:orientation">vertical</item>
		<item name="android:paddingBottom">30dp</item>
		<item name="android:paddingTop">20dp</item>
	</style>

[layout-to-style]: /layout-to-style/
